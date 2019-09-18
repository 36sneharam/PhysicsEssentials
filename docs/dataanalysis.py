import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
import basicplot as bp
import numpy as np

class analysis():
    def __init__(self, plot):
        self.plot = plot
    def linreg(self):
        x = self.plot.x
        y = self.plot.y
        x = np.reshape(x,(len(x),1)) #Reshaping for Linear Regression
        y = np.reshape(y,(len(y),1)) 
        reg = LinearRegression()
        reg.fit(x,y)
        ypred = reg.predict(x)
        
        """
        x = np.reshape(x,(1,len(x))) #Undoing reshaping
        ypred = np.reshape(ypred,(1,len(ypred))) #Undoing reshaping
        x.tolist()
        ypred.tolist()
        """
        return [x,ypred]
    def plotlinreg(self):
        [x, ypred] = self.linreg()
        self.plot.plotscatter(clear = False)
        self.plot.gety(ypred)
        self.plot.getx(x)
        self.plot.plotscatter(clear = True, marker = '--')

#Formatting 
plt.close()

#Initializing plot 
x = np.linspace(0,10, 10)
y = np.linspace(0, 20, 10)
p1 = bp.plot(x, y, "Test Reg", "x","y")

#Plotting fit 
a1 = analysis(p1)
a1.plotlinreg()

"""
a1 = analysis(p1) 
[x, ypred] = a1.linreg()

#Plotting plot
p1.plotscatter(clear = False)
p1.gety(ypred)
p1.getx(x)
p1.plotscatter(clear = True, marker = '--')
"""
