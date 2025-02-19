import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

plt.rcParams["text.usetex"] = True

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

def hash(n,m):
    return p[(p[n%256]+m)%256]

def calc_grad(n,m):
    h=hash(n,m)&0b111
    return grad[h]

def hash(n):
    return p[n%256]

g=[0.25,0.5,0.75,1,-0.25,-0.5,-0.75,-1]

def calc_grad(n):
    h=hash(n)
    return g[h&0b111]

X=np.arange(0,4,1)
Y=np.arange(0,1,1)
X,Y=np.meshgrid(X,Y,indexing="ij") #X[nx,ny],Y[nx,ny]
U=np.zeros(X.shape)
V=np.zeros(X.shape)
for nx in range(X.shape[0]):
    for ny in range(X.shape[1]):
        U[nx,ny]=calc_grad(nx)
        V[nx,ny]=0

fig,ax=plt.subplots(figsize=(5,1))
ax.hlines(0,0,4,color=(0,0,0,0.5),lw=2)
ax.quiver(X,Y,U,V,angles="xy",
          scale_units="xy",scale=1,clip_on=False,
          color="red",width=0.012,zorder=2)
plt.subplots_adjust(left=0.20,right=0.80)

ax.text(-0.5,0,r"$\vec v_0$",va="bottom",ha="center",fontsize=18,color="red")
ax.text(1.1,0.05,r"$\vec v_1$",va="bottom",ha="center",fontsize=18,color="red")
ax.text(2.2,0.05,r"$\vec v_2$",va="bottom",ha="center",fontsize=18,color="red")
ax.text(3.5,0.05,r"$\vec v_3$",va="bottom",ha="center",fontsize=18,color="red")

ax.axis("square")
ax.set_xlabel("x")
#ax.grid("on")
ax.set(xlim=(X.min(),X.max()),ylim=(Y.min(),Y.max()))
ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
ax.get_yaxis().set_ticks([])
ax.set(frame_on=False) 
#plt.savefig("lattice-gradient-2d.svg")
plt.show()
