import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *
from matplotlib import patches

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

def calc_grad(n):
    h=hash(n)
    g=0.25*((h&0b11)+1)
    h&2 and (g:=-g)
    return g

fig,ax=plt.subplots(figsize=(5,1))

def arrow(x,y,dx,dy,color):
    options={"x":x,"y":y,"dx":dx,"dy":dy,"width":0.03,
             "color":color,
             "length_includes_head":True,
             "overhang":0.1,
             "head_length":0.15,
             "clip_on":False}
    arrow = patches.FancyArrow(**options)
    ax.add_patch(arrow)

ax.hlines(0,0,3,color=(0,0,0,0.5),lw=2,clip_on=False)
plt.subplots_adjust(left=0.20,right=0.80)


arrow(0,0,calc_grad(0),0,color="red")
arrow(1,0,calc_grad(1),0,color="red")
arrow(2,0.05,calc_grad(2),0,color="red")
arrow(3,-0.05,calc_grad(3),0,color="red")


ax.text(-0.5,0,r"$\vec v_0$",va="bottom",ha="center",fontsize=18,color="red")
ax.text(1.1,0.05,r"$\vec v_1$",va="bottom",ha="center",fontsize=18,color="red")
ax.text(2.2,0.07,r"$\vec v_2$",va="bottom",ha="center",fontsize=18,color="red")
ax.text(2.5,-0.05,r"$\vec v_3$",va="top",ha="center",fontsize=18,color="red")

ax.axis("square")
ax.set_xlabel("x")
#ax.grid("on")
ax.set(xlim=(0,3),ylim=(0,0.1))
ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
ax.get_yaxis().set_ticks([])
ax.set(frame_on=False) 
#plt.savefig("lattice-gradient-2d.svg")
plt.show()
