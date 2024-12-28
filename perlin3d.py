import numpy as np
from mayavi import mlab
from tvtk.api import tvtk

#set up the initial gradients for all lattice points
N=256
rng = np.random.default_rng()
def unit_vector():
    v=rng.uniform(-1,1,3)
    l=np.linalg.norm(v)
    if l==0.0:
        return v
    return v/l

g=np.empty((N+1,N+1,N+1,3)) #the indexing is g[nz][ny][nx]
for ny in range(N+1):
    for nx in range(N+1):
        g[0][ny][nx]=unit_vector()

for nz in range(1,N+1):
    g[nz,:,:]=g[0,:,:]
    rng.shuffle(g[nz,:,:],axis=1)
    rng.shuffle(g[nz,:,:],axis=2)

from test_gradients import test_gradients_3d
g[0:4,0:4,0:4,:]=test_gradients_3d

#s curve
def s(r):
    return 3.0*r**2-2*r**3

#perlin 3d
def perlin(x,y,z):
    #x=x+4096 #to allow x to range from -4096
    x=x%N #to allow x to have no upper limit
    nx=int(x) #decimal part of x
    rx=x-int(x) #fractional part of x
    
    #y=y+4096 #to allow y to range from -4096
    y=y%N #to allow y to have no upper limit
    ny=int(y) #decimal part of y
    ry=y-int(y) #fractional part of y

    #z=z+4096 #to allow z to range from -4096
    z=z%N #to allow z to have no upper limit
    nz=int(z) #decimal part of z
    rz=z-int(z) #fractional part of z

    #the indexing of suffix is w_zyx
    w000=np.dot(g[nz  ][ny  ][nx  ],(rx  ,ry  ,rz  ))
    w001=np.dot(g[nz  ][ny  ][nx+1],(rx-1,ry  ,rz  ))
    w010=np.dot(g[nz  ][ny+1][nx  ],(rx  ,ry-1,rz  ))
    w011=np.dot(g[nz  ][ny+1][nx+1],(rx-1,ry-1,rz  ))
    w100=np.dot(g[nz+1][ny  ][nx  ],(rx  ,ry  ,rz-1))
    w101=np.dot(g[nz+1][ny  ][nx+1],(rx-1,ry  ,rz-1))
    w110=np.dot(g[nz+1][ny+1][nx  ],(rx  ,ry-1,rz-1))
    w111=np.dot(g[nz+1][ny+1][nx+1],(rx-1,ry-1,rz-1))

    return w000*(1-s(rx))*(1-s(ry))*(1-s(rz))+\
           w001*(  s(rx))*(1-s(ry))*(1-s(rz))+\
           w010*(1-s(rx))*(  s(ry))*(1-s(rz))+\
           w011*(  s(rx))*(  s(ry))*(1-s(rz))+\
           w100*(1-s(rx))*(1-s(ry))*(  s(rz))+\
           w101*(  s(rx))*(1-s(ry))*(  s(rz))+\
           w110*(1-s(rx))*(  s(ry))*(  s(rz))+\
           w111*(  s(rx))*(  s(ry))*(  s(rz))

#make the plot data
MAX=3.0
x=y=z=np.arange(0,MAX+0.2,0.2)
x,y,z=np.meshgrid(x,y,z,indexing="ij") #the indexing is x[nx,ny,nz]
w=np.empty(x.shape)
for nx in range(x.shape[0]):
    for ny in range(x.shape[1]):
        for nz in range(x.shape[2]):
            w[nx,ny,nz]=perlin(x[nx,ny,nz],y[nx,ny,nz],z[nx,ny,nz])

#plot them
fig=mlab.figure()
contour=mlab.contour3d(x,y,z,w,transparent=True,contours=50)#render the contour. the indexing must be x[nx,ny,nz]

#show the axes
mlab.axes(extent=[0,MAX,0,MAX,0,MAX],ranges=[0,MAX,0,MAX,0,MAX])

#show the color bar
scalar_bar=tvtk.ScalarBarActor()
fig.scene.renderer.add_actor2d(scalar_bar)

#make the color lookup table
HI=0.8
LO=-0.8
TS=256
ctf=tvtk.ColorTransferFunction()
ctf.add_rgb_point(LO,0,0,1) #the low values show blue
ctf.add_rgb_point((HI+LO)/2,1,1,1) #near zero values show white
ctf.add_rgb_point(HI,1,0,0) #the high values show red
lut=tvtk.LookupTable()
lut.table_range=[LO,HI]
lut.table=[np.array((ctf.get_color(LO+i*(HI-LO)/TS)+(0.5,)))*255 for i in np.arange(TS+1)]
#set it
contour.actor.mapper.lookup_table=lut
scalar_bar.lookup_table=lut

#show the lattice grid
GS=MAX+1
append= tvtk.AppendPolyData()
for i in np.arange(GS):
    image=tvtk.ImageData(dimensions=(GS,GS,1),spacing=(1,1,1),origin=(0,0,i))
    surface=tvtk.DataSetSurfaceFilter()
    surface.set_input_data(image)
    append.add_input_connection(surface.output_port)

    image=tvtk.ImageData(dimensions=(GS,1,GS),spacing=(1,1,1),origin=(0,i,0))
    surface=tvtk.DataSetSurfaceFilter()
    surface.set_input_data(image)
    append.add_input_connection(surface.output_port)

mapper=tvtk.PolyDataMapper()
mapper.set_input_connection(append.output_port)
p=tvtk.Property(opacity=1,color=(1,1,1),ambient=1,representation="wireframe",line_width=1)
actor=tvtk.Actor(mapper=mapper,property=p)
fig.scene.add_actor(actor)
