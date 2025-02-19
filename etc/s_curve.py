import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

def s(r):
    return 6*r**5-15*r**4+10*r**3

fig=plt.figure(figsize=(4,4),layout="constrained") # inch
ax=fig.add_subplot()
ax.set_ylabel("y")
ax.set_xlabel("r")

x=np.linspace(0,1,100)
y=[s(x) for x in x]
ax.plot(x,y,color="blue",clip_on=False)
y=[1-s(x) for x in x]
ax.plot(x,y,color="red",clip_on=False)


ax.grid("on")
ax.set(ylim=(0,1),xlim=(0,1))

ax.text(0.35,0.7,r"$1-s(r)$",va="center",ha="right",fontsize=20,color="red")
ax.text(0.7,0.7,r"$s(r)$",va="center",ha="left",fontsize=20,color="blue")


#ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
#ax.yaxis.set_major_locator(MultipleLocator(base=1.0))
plt.savefig("s_curve.svg")
plt.show()
