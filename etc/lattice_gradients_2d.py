import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

#test gradient
from test_gradients import *
g=test_gradients_2d #g[ny][nx]
        
X=Y=np.arange(0,4,1)
X,Y=np.meshgrid(X,Y,indexing="ij") #X[nx,ny],Y[nx,ny]
U=np.zeros(X.shape)
V=np.zeros(X.shape)
for nx in range(X.shape[0]):
    for ny in range(X.shape[1]):
        U[nx,ny]=g[ny][nx][0]
        V[nx,ny]=g[ny][nx][1]

fig,ax=plt.subplots(figsize=(5,5))
q=ax.quiver(X,Y,U,V,angles="xy",scale_units="xy",scale=1,clip_on=False,color="red")
plt.subplots_adjust(left=0.20,right=0.80)
ax.axis("square")
ax.set_ylabel("y")
ax.set_xlabel("x")
ax.grid("on")
ax.set(xlim=(X.min(),X.max()),ylim=(Y.min(),Y.max()))
ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
ax.yaxis.set_major_locator(MultipleLocator(base=1.0))
plt.savefig("lattice-gradient-2d.svg")
plt.show()
