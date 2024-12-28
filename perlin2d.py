import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *
from matplotlib import cm, ticker

#set up the initial gradients for all lattice points
N=256
gen = np.random.default_rng()
def unit_vector():
    v=gen.uniform(-1,1,2)
    l=np.linalg.norm(v)
    if l==0.0:
        return v
    return v/l

g=np.empty((N+1,N+1,2))
for i in range(N+1):
    for j in range(N+1):
        g[i][j]=unit_vector()

#from test_gradients import test_gradients_2d
#g[0:4,0:4,:]=test_gradients_2d

#s curve
def s(r):
    return 3.0*r**2-2*r**3

#perlin 2d
def perlin(x,y):
    x=x+4096 #to allow x to range from -4096
    x=x%N #to allow x to have no upper limit
    nx=int(x) #decimal part of x
    rx=x-int(x) #fractional part of x
    
    y=y+4096 #to allow y to range from -4096
    y=y%N #to allow y to have no upper limit
    ny=int(y) #decimal part of y
    ry=y-int(y) #fractional part of y

    #z_yx
    z00=np.dot(g[ny  ][nx  ],(rx  ,ry  ))
    z01=np.dot(g[ny  ][nx+1],(rx-1,ry  ))
    z10=np.dot(g[ny+1][nx  ],(rx  ,ry-1))
    z11=np.dot(g[ny+1][nx+1],(rx-1,ry-1))

    return z00*(1-s(rx))*(1-s(ry))+ \
           z01*(  s(rx))*(1-s(ry))+ \
           z10*(1-s(rx))*(  s(ry))+ \
           z11*(  s(rx))*(  s(ry))

#plot data
X=Y=np.arange(0,3.01,0.05)
X,Y=np.meshgrid(X,Y)
Z=np.empty(X.shape)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i,j]=perlin(X[i,j],Y[i,j])

#plot them
#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#ax.plot_surface(X,Y,Z)
fig, ax = plt.subplots(figsize=(6,6),layout="constrained")
level=np.arange(-0.8,0.81,0.05)
CS=ax.contourf(X,Y,Z,level,cmap="bwr")
cbar=fig.colorbar(CS,shrink=0.75)
cbar.set_ticks([-0.8,0.0,0.8])
ax.axis("square")
ax.grid("on")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
ax.yaxis.set_major_locator(MultipleLocator(base=1.0))
plt.savefig("perlin-2d-sample.svg")
plt.show()
