import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d, Axes3D
import numpy as np
import os
#import coordtrans as coord

class plot:
    def __init__(self, x, y, title = "title", xaxis = "xaxis", yaxis = "yaxis", coord = "Cart"):
        self.x = x 
        self.y = y 
        self.title = title
        self.xaxis = xaxis 
        self.yaxis = yaxis
        self.vfield = [0,0,0]
        self.coord = coord
    def getx(self, x):
        self.x = x
    def gety(self, y):
        self.y = y
      
    def plotscatter (self, save = False, impath = "../testplots/test.png", marker = 'o', clear = True):
        
        plt.plot(self.x, self.y, marker)
        plt.xlabel(self.xaxis)
        plt.ylabel(self.yaxis) 
        plt.title(self.title) 
        if save == True:
            plt.savefig(impath)
        else:
            if clear == True:
                plt.show()
    def plot3D (self, z, zaxis = "zaxis", type = "line"):
        fig = plt.figure()
        ax = plt.axes(projection="3d")

        if type == "scatter":
            ax.scatter3D(self.x, self.y, z, c=z, cmap='hsv')
        elif type == "line":
            ax.plot3D(self.x, self.y, z, 'grey')
        elif type == "wireframe":
            X, Y = np.meshgrid(x,y)
            Z = z(X,Y)
            ax.plot_wireframe(X,Y,Z, color = 'green')
        elif type == "surface":
            X, Y = np.meshgrid(x,y)
            Z = z(X,Y)
            ax.plot_surface(X,Y,Z, cmap = 'winter', rstride = 1, cstride = 1)
            
        #Apply Labels
        ax.set_xlabel(self.xaxis)
        ax.set_ylabel(self.yaxis)
        ax.set_zlabel(zaxis)
        ax.set_title(self.title)
        plt.show() 
        

        
    def getvectorfield(self, vfield):
        self.vfield = vfield 
        
    def plotvectorfield(self, save = False, impath = "../testplots/test.png"): 
        
        X,Y = np.meshgrid(self.x,self.y)
        u = self.vfield[0](X,Y)
        v = self.vfield[1](X,Y)
        f = plt.figure()        
        ax = f.add_subplot(111)
        ax.quiver(X,Y,u,v)
        ax.set_xlabel(self.xaxis)
        ax.set_ylabel(self.yaxis)
        ax.set_title(self.title)
        if save == True:
            plt.savefig(impath)
        else:
            plt.show()
    
    
        


"""

#Plotting Simple Scatter Plot
p1 = plot(np.linspace(0,10,100), np.linspace(0, 10,100), "Testing Save feature", "xaxis label","yaxis label")
p1.plotscatter(save = True, impath = "../testplots/a1.jpeg", marker = "x")
"""

"""
#Plotting vector fields (cartesian) 
x = np.linspace(-10, 10, 10)
y = np.linspace(-20, 20, 10) 
F =  [lambda x, y: x, lambda x, y: y, 0]
p1 = plot(x, y, "Test", "x", "y") 
p1.getvectorfield(F) 
p1.plotvectorfield()
"""

#Needs work

"""
#Plotting vector fields (Polar) 

r = np.linspace(-1, 1, 10)
theta = np.linspace(0, 2*np.pi, 10) 
phi = 0 
F = lambda r, theta: np.array([ r,  theta, 0] ) . reshape(3,1)
p2 = plot(r, theta, "Test2", "r", "theta") 
p2.getvectorfield(F)
c2 = coord.coordtrans()
c2.sph_car(p2)
"""
"""
#Plotting 3D graph 

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)


#x = np.linspace(-6,6,30)
#y = np.cos(x)
p1 = plot(x,y)
p1.plot3D(z = lambda x, y: np.sin(np.sqrt(x**2+y**2)), type = 'surface')
"""


