import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

#s curve
def s(r):
    return 6*r**5-15*r**4+10*r**3

#perlin 2d
def perlin2d(x,y):
    n=int(x) #decimal part of x
    rx=x-n #fractional part of x
    
    m=int(y) #decimal part of y
    ry=y-m #fractional part of y

    z0=calc_grad_dot(n  ,m  ,rx  ,ry  )
    z1=calc_grad_dot(n+1,m  ,rx-1,ry  )
    z2=calc_grad_dot(n  ,m+1,rx  ,ry-1)
    z3=calc_grad_dot(n+1,m+1,rx-1,ry-1)

    return z0*(1-s(rx))*(1-s(ry))+\
           z1*(  s(rx))*(1-s(ry))+\
           z2*(1-s(rx))*(  s(ry))+\
           z3*(  s(rx))*(  s(ry))

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

def calc_grad_dot(n,m,x,y):
    h=hash(n,m)%12
    h&4 and (u:=y,v:=x) or (u:=x,v:=y)
    h>3 and (v:=0)
    h&1 and (u:=-u)
    h&2 and (v:=-v)
    return u+v

if __name__=="__main__":
    #make plot data
    MAX=3
    X=Y=np.arange(0,MAX+0.01,0.05)
    X,Y=np.meshgrid(X,Y,indexing="ij") #x[nx,ny]
    Z=np.empty(X.shape)
    for nx in range(X.shape[0]):
        for ny in range(X.shape[1]):
            Z[nx,ny]=perlin2d(X[nx,ny],Y[nx,ny])

    #plot them
    fig, ax = plt.subplots(figsize=(6,6),layout="constrained")
    level=np.arange(-0.81,0.81,0.01)
    CS=ax.contourf(X,Y,Z,level,cmap="bwr")
    cbar=fig.colorbar(CS,shrink=0.75)
    cbar.set_ticks([-0.8,0.8])
    ax.axis("square")
    ax.grid("on")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
    ax.yaxis.set_major_locator(MultipleLocator(base=1.0))
    #plt.savefig("perlin-2d-sample.svg")
    plt.show()
