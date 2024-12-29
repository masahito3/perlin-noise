import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

#test gradient
g=[[[ 0.80657968, -0.59112538],
    [-0.97915435,  0.20311758],
    [-0.12766751,  0.99181702],
    [-0.77859   ,  0.62753295]],
   [[-0.57106799,  0.82090277],
    [-0.21321278, -0.97700579],
    [-0.63945014,  0.76883257],
    [-0.93657184, -0.35047566]],
   [[-0.75685024,  0.65358834],
    [0.68717107 ,  0.72649564],   
    [ 0.29387598, -0.95584356],
    [-0.77991784,  0.62588191]],
   [[-0.77802389, -0.62823469],
    [-0.30530758, -0.95225379],
    [ 0.72762537, -0.68597472],
    [ 0.7652237 ,  0.64376446]]]
        
X=Y=np.arange(0, 10, 1)
X,Y=np.meshgrid(X,Y)
U=np.zeros(X.shape)
V=np.zeros(X.shape)

for i in range(4):
    for j in range(4):
        U[i,j]=g[i][j][0]
        V[i,j]=g[i][j][1]


fig,ax=plt.subplots(figsize=(7,7))#,layout="constrained")
q=ax.quiver(X,Y,U,V,angles="xy",scale_units="xy",scale=1,clip_on=False,color="red")
plt.subplots_adjust(left=0.35, right=0.65, bottom=0.35, top=0.65)

ax.set_ylabel("y")
ax.set_xlabel("x")
ax.grid("on")
ax.set(xlim=(0,1),ylim=(0,1))
ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
ax.yaxis.set_major_locator(MultipleLocator(base=1.0))
plt.savefig("gradient-sample-2d.svg")
plt.show()
