import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

def s(t):
    return 3.0*t**2-2*t**3


fig=plt.figure(figsize=(4,4),layout="constrained") # inch
ax=fig.add_subplot()
ax.set_ylabel("y")
ax.set_xlabel("r")

x=np.linspace(0,1,100)
y=[s(x) for x in x]
ax.plot(x,y,color="blue")
y=[1-s(x) for x in x]
ax.plot(x,y,color="red")


ax.grid("on")
ax.set(ylim=(0,1),xlim=(0,1))
#ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
#ax.yaxis.set_major_locator(MultipleLocator(base=1.0))
plt.savefig("s_curve.svg")
plt.show()
