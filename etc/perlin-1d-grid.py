import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.path import Path

plt.rcParams["text.usetex"] = True

fig,ax = plt.subplots(figsize=(6,3))

ax.plot(1.6,0,marker="o",color="green")
ax.plot(1,0,marker="o",color="green")
ax.plot(2,0,marker="o",color="green")

def arrow(x,y,dx,dy,color):
    options={"x":x,"y":y,"dx":dx,"dy":dy,"width":0.06,
             "color":color,
             "length_includes_head":True,
             "overhang":0.1,
             "head_length":0.13}
    arrow = patches.FancyArrow(**options)
    ax.add_patch(arrow)

arrow(1,0,0.6,0,(0,0,0,0.3))
arrow(2,0,-0.4,0,(0,0,0,0.3))
    
verts1=np.array([[1,0],[1.3,-0.3], [1.6,0]])
codes1=[Path.MOVETO,Path.CURVE3,Path.CURVE3]
path1=Path(verts1, codes1)
patch1=patches.PathPatch(path1, edgecolor='black', facecolor=(0,0,0,0),lw=1)
ax.add_patch(patch1)

line=plt.Polygon([(0,0),(3,0)],facecolor=(0,0,0,0),edgecolor=(0,0,0),lw=2)
ax.add_patch(line)

ax.set(ylim=(-1,1))
ax.set(xlim=(0.5,2.5))

ax.text(1.6,0,r"$P$",va="bottom",ha="center",fontsize=20)
ax.text(1,0,r"$O_0$",va="bottom",ha="center",fontsize=20)
ax.text(2,0,r"$O_1$",va="bottom",ha="center",fontsize=20)

ax.text(1.6,-0.05,r"$x$",va="top",ha="center",fontsize=20)
ax.text(1,-0.05,r"$n$",va="top",ha="center",fontsize=20)
ax.text(2,-0.05,r"$n\!+\!1$",va="top",ha="center",fontsize=20)

ax.text(1.3,-0.15,r"$r$",va="top",ha="center",fontsize=20)

#ax.text(1,0.8,r"$n=int(x)$",va="bottom",ha="left",fontsize=20)
#ax.text(1,0.5,r"$r=x-int(x)$",va="bottom",ha="left",fontsize=20)

ax.axis("off")
plt.show()
