import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.path import Path

plt.rcParams["text.usetex"] = True

fig,ax = plt.subplots(figsize=(5,5))

def arrow(x,y,dx,dy,color):
    options={"x":x,"y":y,"dx":dx,"dy":dy,"width":0.03,
             "color":color,
             "length_includes_head":True,
             "overhang":0.1,
             "head_length":0.15}
    arrow = patches.FancyArrow(**options)
    ax.add_patch(arrow)

def line(x0,y0,x1,y1,color="black",lw=2):
    line=plt.Polygon([(x0,y0),(x1,y1)],
                     facecolor=(0,0,0,0),edgecolor=color,lw=lw)
    ax.add_patch(line)

line(0,0,3,0)
line(0,0,0,3)

ax.plot(1.6,1.5,marker="o",color="green")
ax.plot(1,1,marker="o",color="green")
ax.plot(2,1,marker="o",color="green")
ax.plot(1,2,marker="o",color="green")
ax.plot(2,2,marker="o",color="green")

box=plt.Rectangle((1,1),1,1,facecolor=(0,0,0,0),edgecolor="black",lw=2)
ax.add_patch(box)

arrow(1,1,0.6,0.5,color=(0,0,0,0.3))
arrow(2,1,-0.4,0.5,color=(0,0,0,0.3))
arrow(1,2,0.6,-0.5,color=(0,0,0,0.3))
arrow(2,2,-0.4,-0.5,color=(0,0,0,0.3))


line(1.6,0,1.6,1.5,color=(0,0,0,0.3),lw=1)
line(0,1.5,1.6,1.5,color=(0,0,0,0.3),lw=1)

line(1,0,1,1,lw=1)
line(2,0,2,1,lw=1)
line(0,1,1,1,lw=1)
line(0,2,1,2,lw=1)

verts1=np.array([[1,0],[1.3,0.3], [1.6,0]])
codes1=[Path.MOVETO,Path.CURVE3,Path.CURVE3]
path1=Path(verts1, codes1)
patch1=patches.PathPatch(path1, edgecolor='black', facecolor=(0,0,0,0),lw=1)
ax.add_patch(patch1)

verts1=np.array([[0,1],[0.2,1.25], [0,1.5]])
codes1=[Path.MOVETO,Path.CURVE3,Path.CURVE3]
path1=Path(verts1, codes1)
patch1=patches.PathPatch(path1, edgecolor='black', facecolor=(0,0,0,0),lw=1)
ax.add_patch(patch1)

#ax.set(ylim=(-1,1))
#ax.set(xlim=(0.5,2.5))

ax.text(1.6,1.5,r"$P$",va="bottom",ha="center",fontsize=20)

ax.text(1,1,r"$O_0$",va="top",ha="right",fontsize=20)
ax.text(2,1,r"$O_1$",va="top",ha="left",fontsize=20)
ax.text(1,2,r"$O_2$",va="bottom",ha="right",fontsize=20)
ax.text(2,2,r"$O_3$",va="bottom",ha="left",fontsize=20)

ax.text(1.6,-0.05,r"$x$",va="top",ha="center",fontsize=20)
ax.text(1,-0.05,r"$n$",va="top",ha="center",fontsize=20)
ax.text(2,-0.05,r"$n\!+\!1$",va="top",ha="center",fontsize=20)
ax.text(1.3,0.15,r"$r_x$",va="bottom",ha="center",fontsize=20)

ax.text(-0.05,1.5,r"$y$",va="center",ha="right",fontsize=20)
ax.text(-0.05,1,r"$m$",va="center",ha="right",fontsize=20)
ax.text(-0.05,2,r"$m\!+\!1$",va="center",ha="right",fontsize=20)
ax.text(0.2,1.25,r"$r_y$",va="center",ha="left",fontsize=20)

#ax.text(1,0.8,r"$n=int(x)$",va="bottom",ha="left",fontsize=20)
#ax.text(1,0.5,r"$r=x-int(x)$",va="bottom",ha="left",fontsize=20)

ax.axis("off")
plt.show()
