import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

# initialize
N=256
gen = np.random.default_rng()
g=gen.uniform(-1,1,N+1)

#from etc.test_gradients import test_gradients_1d
#g[0:10]=test_gradients_1d

def s(r):
    return 3.0*r**2-2*r**3

def perlin(x):
    x=x+4096 #to allow x to range from -4096
    x=x%N #to allow x to have no upper limit
    n=int(x) #decimal part
    r=x-int(x) #fractional part
    y0=g[n]*r
    y1=g[n+1]*(r-1)
    return y0*(1-s(r))+y1*s(r)

if __name__=="__main__":
    #plot data
    x=np.arange(0,4,0.01)
    y=[perlin(x) for x in x]

    #plot
    fig=plt.figure(figsize=(8,3),layout="constrained") # inch
    ax=fig.add_subplot()
    ax.plot(x,y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid("on")
    ax.set(ylim=(-0.5,0.5))
    ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
    ax.yaxis.set_major_locator(MultipleLocator(base=0.5))
    plt.savefig("perlin-1d-sample.svg")
    plt.show()
