import numpy as np
from mayavi import mlab
from tvtk.api import tvtk
import inspect

#append= tvtk.AppendPolyData()
#image=tvtk.ImageData(dimensions=(4,4,1),spacing=(1,1,1),origin=(0,0,0)) # (x,y,z)
#surface=tvtk.DataSetSurfaceFilter()
#surface.set_input_data(image)
#append.add_input_connection(surface.output_port)
#image=tvtk.ImageData(dimensions=(4,4,1),spacing=(1,1,1),origin=(0,0,1)) # (x,y,z)
#surface=tvtk.DataSetSurfaceFilter()
#surface.set_input_data(image)
#append.add_input_connection(surface.output_port)
#image=tvtk.ImageData(dimensions=(4,4,1),spacing=(1,1,1),origin=(0,0,2)) # (x,y,z)
#surface=tvtk.DataSetSurfaceFilter()
#surface.set_input_data(image)
#append.add_input_connection(surface.output_port)

append= tvtk.AppendPolyData()
N=4
for i in range(N):
    image=tvtk.ImageData(dimensions=(N,N,1),spacing=(1,1,1),origin=(0,0,i)) # (x,y,z)
    surface=tvtk.DataSetSurfaceFilter()
    surface.set_input_data(image)
    append.add_input_connection(surface.output_port)

    image=tvtk.ImageData(dimensions=(N,1,N),spacing=(1,1,1),origin=(0,i,0)) # (x,y,z)
    surface=tvtk.DataSetSurfaceFilter()
    surface.set_input_data(image)
    append.add_input_connection(surface.output_port)

    
#filter=tvtk.ImageDataGeometryFilter()
#filter.set_input_data(image)
#outline=tvtk.ImageDataOutlineFilter()
#outline.set_input_data(image)


#slice=tvtk.ImageReslice()
#slice.set_input_data(image)

#plane=tvtk.PlaneSource()
#plane.x_resolution=3
#plane.y_resolution=3

#plane.center=np.array([0.0,0.0,0.0])
#plane.point1=np.array([0.,0.,0.])
#plane.point2=np.array([3.,3.,0.])

#points=tvtk.Points()
#points.insert_next_point(0, 0, 0)
#points.insert_next_point(0, 0, 1);
#points.insert_next_point(0, 0, 2);
#polydata=tvtk.PolyData()
#polydata.points=points
#glyph=tvtk.Glyph3D()
##glyph.set_source_connection(plane.output_port)
#glyph.set_source_connection(surface.output_port)
#glyph.set_input_data(polydata)


#grid=tvtk.ImageGridSource()
#grid.fill_value=122
#grid.update()
#image_cast=tvtk.ImageCast()
#image_cast.set_input_connection(grid.output_port)
#image_cast.set_output_scalar_type_to_unsigned_char()
#image_cast.update()

mapper=tvtk.PolyDataMapper()
mapper.set_input_connection(append.output_port)
#mapper.set_input_connection(glyph.output_port)
#mapper.set_input_connection(plane.output_port)
#mapper.set_input_connection(outline.output_port)
#mapper.set_input_connection(filter.output_port)
#mapper.set_input_connection(slice.output_port)

fig=mlab.figure()
p = tvtk.Property(opacity=1,color=(1,1,1),ambient=0.7,representation="wireframe")
actor=tvtk.Actor(mapper=mapper,property=p)
fig.scene.add_actor(actor)

#actor=tvtk.ImageActor()
#actor.mapper.set_input_connection(image_cast.output_port)
MAX=4
x=y=z=np.arange(0,4,0.2)
x,y,z=np.meshgrid(x,y,z,indexing="ij")
w=0.0*x
mlab.contour3d(x,y,z,w,transparent=True)
#mlab.axes(extent=[0,MAX,0,MAX,0,MAX],ranges=[0,MAX,0,MAX,0,MAX])
axes=mlab.axes(extent=[0,MAX,0,MAX,0,MAX],ranges=[0,MAX,0,MAX,0,MAX])

fig.scene.camera.position=np.array([MAX*1.5,MAX*2,MAX*1.5])
fig.scene.camera.focal_point=np.array([MAX/2,MAX/2,MAX/2])
fig.scene.camera.view_angle=30

#c=tvtk.ColorSeries()
#c.color_scheme=16 #the color scheme numbers are written in the vtk document


#show grid using poly data
#points=np.empty([N*N*2,3])
#lines=np.empty([N*N,2])
#i=j=0
#for ny in np.arange(N):
#    for nx in np.arange(N):
#        points[i  ]=[nx,ny,0]
#        points[i+1]=[nx,ny,N-1]
#        lines[j]=[i,i+1]
#        i+=2
#        j+=1
#points=np.concatenate([points,points[:,[0,2,1]],points[:,[2,0,1]]])
#lines=np.concatenate([lines,lines+N*N*2,lines+N*N*2*2])        
#fig=mlab.figure()
#data=tvtk.PolyData(points=points,lines=lines)
#mapper=tvtk.PolyDataMapper()
#mapper.set_input_data(data)
#p = tvtk.Property(opacity=1,color=(1,1,1),ambient=0.7,representation="wireframe")
#actor=tvtk.Actor(mapper=mapper,property=p)
#fig.scene.add_actor(actor)

#mlab.gcf().scene.camera    
#fig.scene.camera



#vtkColorTransferFunction can be set to mapper's, actor's lookup table but
#the colors has only fixed alpha of 1, can't change.
#so hoped the alpha changes, use vtkLookupTable
#and set the colors and alphas one by one
#the colors might be get from vtkColorTransferFunction
#ctf=tvtk.ColorTransferFunction()
#ctf.add_rgb_point(w.min(),0,0,1)
#ctf.add_rgb_point(w.max(),1,0,0)
#contour.actor.mapper.lookup_table=ctf
#scalar_bar.lookup_table=ctf
#vtkColorSeries also can't treat alpha.

#lut=tvtk.LookupTable()
#lut.table_range=[MI,MX]
#lut.table=[np.array((ctf.get_color(MI+i*(MX-MI)/TS)+(0.5,)))*255 for i in np.arange(TS+1)] #memo: in lut.table the rgb ranges 0 to 255
# or
#lut.number_of_table_values=TS
#lut.build()
#for i in range(TS+1):
#    rgb=ctf.get_color(MI+i*(MX-MI)/TS)
#    lut.set_table_value(i,rgb+(0.5,)) #this rgb ranges 0 to 1


#lut.table_range=[-1,1] #[-0.38540824,  0.37454609])
##lut.hue_range=[0.66667,0]
#lut.alpha_range=[0.1,0.1]
##lut.ramp='sqrt' #sqrt,s_curve,linear
#lut.build()


#fig=mlab.figure()
#mlab.mesh(x,y,z,color=(1,1,1),representation="wireframe")
#mlab.pipeline.user_defined(x,y,z,u,v,w, filter=tvtk.RectilinearGrid())
#mlab.pipeline.user_defined(filter=tvtk.RectilinearGrid())
#mlab.show()

#how to research vtk classes,functions and their args
#color=tvtk.ColorTransferFunction()
#to see the class methods
# dir(color)
# ..., add_rgb_point,...
#to show the function args
# import inspect
# inspect.signature(color.add_rgb_point)
# <Signature (*args)>
#however there is nothing to be gained
#then to see the function args,go to source code
#the source code is here /usr/lib/python3/dist-packages/tvtk/tvtk_classes.zip/color_transfer_function.py
# and there is a comment about args
# def add_rgb_point(self,*args):
#    """
#    add_rgb_point(self, x:float, r:float, g:float, b:float) -> int
#    ...
# and see the vtk documents of course
# and search the vtk examples in https://examples.vtk.org/site/
# this example site has many figures,so it is so comprehensible

#to append PolyData
#append= tvtk.AppendPolyData()
#append.add_input_connection(surface.output_port)
#mapper.set_input_connection(append.output_port)


#scalar_bar=tvtk.ScalarBarActor()
#scalar_bar.number_of_labels=3

#volume rendering
#volume=mlab.pipeline.volume(mlab.pipeline.scalar_field(x,y,z,w)) #volumetric rendering
#mlab.volume_slice(x,y,z,w, plane_orientation='x_axes', slice_index=15)

#isometric view
#fig=mlab.figure()
#fig.scene.parallel_projection = True

