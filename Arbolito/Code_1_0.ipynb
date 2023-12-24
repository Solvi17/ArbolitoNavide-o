############################### Tree version 1 #######################################################
# !pip install numpy
# !pip install matplotlib
# !pip install pillow
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation


%matplotlib
# grafica
fig = plt.figure()
axt = fig.add_subplot(projection='3d')

#datos
thetat = np.linspace(5,6*np.pi, 1000)

rt = np.linspace(0,-6, 1000)
xt = rt* np.cos(6*thetat)
yt = rt* np.sin(6*thetat)
zt = rt* thetat

def actualizar(i):
    
    axt.clear()
    axt.set_zlim(min(zt),max(zt))
    
    # Estrella
    axt.scatter(0,0,max(xt)+10, marker='*', c='yellow', s = 600)
    
    # Arbol
    value = 40*i
    axt.scatter(xt[:i+value],yt[:i+value],zt[:i+value], alpha=0.25, zorder = 1.5, s = 10, c="#034F13")
    
    
    # color bolas
    colors = ('#28cf75', '#3a9bdc', '#BD3634', '#FFFF00')
    n = np.random.randint(0,30)
    
    c_list = []
    for c in colors:
        c_list.extend([c] * n)
        
    # bolas aleatorios
    
    cp = np.random.randint(-6, 6, n*len(colors))
    cp1 = np.random.randint(-4, 6, n*len(colors))
    cp2 = np.random.randint(0, 100, n*len(colors))
    

    x = np.random.sample(n * len(colors))-cp
    y = np.random.sample(n * len(colors))-cp1
    z = np.random.sample(n * len(colors))-cp2

        
    #tamaño bola
    rb = np.random.randint(60,200)
    s_size =  rb * np.random.rand(n*len(colors))
    
    axt.scatter(x, y, z, c=c_list, s = s_size, alpha=0.5)
    
    
    
    axt.set_title("Feliz Navidad para todos")
    axt.set_xlim(min(xt),max(xt))
    axt.set_ylim(min(yt),max(yt))
    axt.set_axis_off()
    
plt.tight_layout(pad=2)
    
animetion = animation.FuncAnimation(fig, actualizar, range(30), interval=100)
animetion.save("movie_1.gif")
plt.show()