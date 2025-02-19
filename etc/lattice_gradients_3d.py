import numpy as np
from mayavi import mlab
from tvtk.api import tvtk

#random number table
p=[151,160,137,91,90,15,
   131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
   190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
   88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
   77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
   102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
   135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
   5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
   223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
   129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
   251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
   49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
   138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]

def hash(n,m,l):
    return p[(p[(p[n%256]+m)%256]+l)%256]

def calc_grad(n,m,l):
    h=hash(n,m,l)&0b1111
    return grad[h]

grad=[
(1,1,0),
(-1,1,0),
(1,-1,0),
(-1,-1,0),
(1,0,1),
(-1,0,1),
(1,0,-1),
(-1,0,-1),
(0,1,1),
(0,-1,1),
(0,1,-1),
(0,-1,-1),
(1,1,0),
(0,-1,1),
(-1,1,0),
(0,-1,-1),
]

N=4

#making plot data
x=y=z=np.arange(0,N)
x,y,z=np.meshgrid(x,y,z,indexing="ij") #the indexing of x is x[nx,ny,nz]. for y,z,u,v,w the same holds 
u=0.0*x
v=0.0*y
w=0.0*z
for nx in range(N):
    for ny in range(N):
        for nz in range(N):
            u[nx,ny,nz]=calc_grad(nz,ny,nx)[0]
            v[nx,ny,nz]=calc_grad(nz,ny,nx)[1]
            w[nx,ny,nz]=calc_grad(nz,ny,nx)[2]

fig=mlab.figure()
#fig.scene.parallel_projection = True
mlab.quiver3d(x,y,z,u,v,w)
mlab.axes(extent=[0,N-1,0,N-1,0,N-1],ranges=[0,N-1,0,N-1,0,N-1])

#show grid using ImageData
append= tvtk.AppendPolyData()
for i in range(N):
    image=tvtk.ImageData(dimensions=(N,N,1),spacing=(1,1,1),origin=(0,0,i)) # (x,y,z)
    surface=tvtk.DataSetSurfaceFilter()
    surface.set_input_data(image)
    append.add_input_connection(surface.output_port)

    image=tvtk.ImageData(dimensions=(N,1,N),spacing=(1,1,1),origin=(0,i,0)) # (x,y,z)
    surface=tvtk.DataSetSurfaceFilter()
    surface.set_input_data(image)
    append.add_input_connection(surface.output_port)

mapper=tvtk.PolyDataMapper()
mapper.set_input_connection(append.output_port)
p = tvtk.Property(opacity=1,color=(1,1,1),ambient=0.7,representation="wireframe")
actor=tvtk.Actor(mapper=mapper,property=p)
fig.scene.add_actor(actor)

fig.scene.camera.position=np.array([9,12,9])
fig.scene.camera.focal_point=np.array([1.5,1.5,1.5])
fig.scene.camera.view_angle=25

mlab.show()

