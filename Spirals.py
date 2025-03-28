import numpy as np
import math
from scipy.integrate import quad
import matplotlib.pyplot as plt

a = [0, -4, 0, 0.33]
def theta(t):
    v = 0.0
    for i in range(len(a)):
        v += a[i]*math.pow(t,i)
    return v

# Use linspace to generate points along the spiral to plot
distances = np.linspace(-10,10,200)
        
normalize_angle = lambda t: math.atan2(math.sin(t),math.cos(t))

fn_x = lambda s: math.cos(theta(s))
fn_y = lambda s: math.sin(theta(s))

x = []
y = []

for d in distances:
    X, error = quad(fn_x,0,d)
    Y, error = quad(fn_y,0,d)
    x.append(X)
    y.append(Y)


plt.plot(x,y)
plt.show()
