import numpy as np

class coordtrans:
    def __init__(self):
        #Defining Transformation Matrices 
        self.Asph2car = lambda theta, phi: np.matrix([[np.cos(theta)*np.cos(phi), np.cos(theta)*np.cos(phi), -np.sin(phi)], [np.sin(theta)*np.sin(phi), np.cos(theta)*np.sin(phi), np.cos(phi)], [np.cos(theta), -np.sin(theta), 0]] )         
    def sph_car(self, plot) :
        r = plot.x
        theta = plot.y 
        x = []
        y = []
        for i in range(0, len(r)):
            for j in range(0,len(theta)):
                #Transforming Coordinates
                x.append(r[i]*np.cos(theta[j]))
                y.append(r[i]*np.sin(theta[j]))
                print(self.Asph2car(theta[j], 0)*plot.vfield(r[i],theta[j]))
            print(x[1])
            print(y[1])
        plot.x = x 
        plot.y = y 
