############################### Tree version 2 #######################################################
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import exp,sin,cos
from pylab import *
import random
import time

%matplotlib


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
a, b = 0.01, 0.02

th = np.linspace(0, 150, 10000)  
x = a * exp(b * th) * cos(th)
y = a * exp(b * th) * sin(th)
z = -1 * np.linspace(0, 2, 10000)
# print(x,y,z)

ax.plot(x, y, z, color="#28cf75")


# Estrella
ax.scatter(0, 0, 0.25, marker="*", c="yellow", s = 600)

def bolas(i):
    
    n = np.random.randint(400, 500)

#     ax.scatter(x[0:x.size: n],y[0:y.size: n], z[0:z.size: n], alpha=1, s=10)

    ax.scatter(x[0:x.size: 100],y[0:y.size: 100], z[0:z.size: 100], alpha=1, s=10)

#     ax.scatter(x[0:x.size: 100],y[0:y.size: 100], z[0:z.size: 100], alpha=0.05, c = "r", s=10)

    ax.scatter(x[0:x.size: 150],y[0:y.size: 150], z[0:z.size: 150], alpha=0.05, c= "r", s=15)


    ax.set_title("Feliz Navidad", c='#2c5b02')
#     print(i)
#     ax.set_axis_off()
    
a = animation.FuncAnimation(fig, bolas, range(10), interval=500, repeat=False)
# a.save("MerryChristmas2.gif")
plt.show()