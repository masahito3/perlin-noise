import numpy as np
from mayavi import mlab
from tvtk.api import tvtk

#s curve
def s(r):
    return 6*r**5-15*r**4+10*r**3

#perlin 3d
def perlin3d(x,y,z):
    n=int(x) #decimal part of x
    rx=x-n #fractional part of x
    
    m=int(y) #decimal part of y
    ry=y-m #fractional part of y

    l=int(z) #decimal part of z
    rz=z-l #fractional part of z

    w0=calc_grad_dot(n  ,m  ,l  ,rx  ,ry  ,rz  )
    w1=calc_grad_dot(n+1,m  ,l  ,rx-1,ry  ,rz  )
    w2=calc_grad_dot(n  ,m+1,l  ,rx  ,ry-1,rz  )
    w3=calc_grad_dot(n+1,m+1,l  ,rx-1,ry-1,rz  )
    w4=calc_grad_dot(n  ,m  ,l+1,rx  ,ry  ,rz-1)
    w5=calc_grad_dot(n+1,m  ,l+1,rx-1,ry  ,rz-1)
    w6=calc_grad_dot(n  ,m+1,l+1,rx  ,ry-1,rz-1)
    w7=calc_grad_dot(n+1,m+1,l+1,rx-1,ry-1,rz-1)

    return w0*(1-s(rx))*(1-s(ry))*(1-s(rz))+\
           w1*(  s(rx))*(1-s(ry))*(1-s(rz))+\
           w2*(1-s(rx))*(  s(ry))*(1-s(rz))+\
           w3*(  s(rx))*(  s(ry))*(1-s(rz))+\
           w4*(1-s(rx))*(1-s(ry))*(  s(rz))+\
           w5*(  s(rx))*(1-s(ry))*(  s(rz))+\
           w6*(1-s(rx))*(  s(ry))*(  s(rz))+\
           w7*(  s(rx))*(  s(ry))*(  s(rz))

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

def calc_grad_dot(n,m,l,x,y,z):
    h=hash(n,m,l)&0b1111
    h<8 and (u:=x) or (u:=y)
    h<4 and (v:=y) or ((h==12 or h==14) and (v:=x) or (v:=z))
    h&1 and (u:=-u)
    h&2 and (v:=-v)
    return u+v

if __name__=="__main__":
    #make the plot data
    MAX=3
    x=y=z=np.arange(0,MAX+0.2,0.2)
    x,y,z=np.meshgrid(x,y,z,indexing="ij") #the indexing is x[nx,ny,nz]
    w=np.empty(x.shape)
    for nx in range(x.shape[0]):
        for ny in range(x.shape[1]):
            for nz in range(x.shape[2]):
                w[nx,ny,nz]=perlin3d(x[nx,ny,nz],y[nx,ny,nz],z[nx,ny,nz])

    #plot them
    fig=mlab.figure()
    #render the contour. the indexing must be x[nx,ny,nz]
    contour=mlab.contour3d(x,y,z,w,transparent=True,contours=50)

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
    mlab.show()
