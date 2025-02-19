import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.path import Path

plt.rcParams["text.usetex"] = True

fig,ax = plt.subplots(figsize=(6,3))

ax.plot(1.6,0,marker="o",color="green")
ax.plot(1,0,marker="o",color="green")
ax.plot(2,0,marker="o",color="green")

def arrow(x,y,dx,dy,color,width=0.05):
    options={"x":x,"y":y,"dx":dx,"dy":dy,"width":width,
             "color":color,
             "length_includes_head":True,
             "overhang":0.1,
             "head_length":0.13}
    arrow = patches.FancyArrow(**options)
    ax.add_patch(arrow)

#verts1=np.array([[1,0],[1.3,-0.3], [1.6,0]])
#codes1=[Path.MOVETO,Path.CURVE3,Path.CURVE3]
#path1=Path(verts1, codes1)
#patch1=patches.PathPatch(path1, edgecolor='black', facecolor=(0,0,0,0),lw=1)
#ax.add_patch(patch1)

def line(x0,y0,x1,y1,color="black",lw=2):
    line=plt.Polygon([(x0,y0),(x1,y1)],
                     facecolor=(0,0,0,0),edgecolor=color,lw=lw)
    ax.add_patch(line)

line(0,0,3,0)
line(1.6,0,1.6,2,(0,0,0,0.3))


arrow(1,0,0.6,0,(0,0,0,0.5),0.07)
arrow(2,0,-0.4,0,(0,0,0,0.5),0.07)

arrow(1,0,0.4,0,"red")
arrow(2,0,-0.3,0,"blue")

line(1,0,1.6,0.85,color="red")
line(2,0,1.6,0.45,color="blue")
    
ax.set(ylim=(-1,1))
ax.set(xlim=(0.5,2.5))

ax.text(1.6,-0.05,r"$P$",va="top",ha="center",fontsize=20)
ax.text(1,-0.05,r"$O_0$",va="top",ha="center",fontsize=20)
ax.text(2,-0.05,r"$O_1$",va="top",ha="center",fontsize=20)

ax.text(1.3,-0.1,r"$\vec v_0$",va="top",ha="center",fontsize=18,color="red")
ax.text(1.85,-0.1,r"$\vec v_1$",va="top",ha="center",fontsize=18,color="blue")

#ax.text(1.61,0.8,r"$y_0=\vec v_0 \cdot \overrightarrow{O_0P}$",
#        va="bottom",ha="left",fontsize=18,color="red")
#ax.text(1.61,0.45,r"$y_1=\vec v_1 \cdot \overrightarrow{O_1P}$",
#        va="bottom",ha="left",fontsize=18,color="blue")

ax.text(1.61,0.8,r"$y_0$",
        va="bottom",ha="left",fontsize=18,color="red")
ax.text(1.61,0.45,r"$y_1$",
        va="bottom",ha="left",fontsize=18,color="blue")

ax.axis("off")
plt.show()
