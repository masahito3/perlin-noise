import numpy as np
from mayavi import mlab
from tvtk.api import tvtk

#gradient data
from test_gradients import test_gradients_3d
g=np.array(test_gradients_3d)

N=g.shape[0]

#making plot data
x=y=z=np.arange(0,N)
x,y,z=np.meshgrid(x,y,z,indexing="ij") #the indexing of x is x[nx,ny,nz]. for y,z,u,v,w the same holds 
u=0.0*x
v=0.0*y
w=0.0*z
for nx in range(N):
    for ny in range(N):
        for nz in range(N):
            u[nx,ny,nz]=g[nz,ny,nx][0]
            v[nx,ny,nz]=g[nz,ny,nx][1]
            w[nx,ny,nz]=g[nz,ny,nx][2]

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

