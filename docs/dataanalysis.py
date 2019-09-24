import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
import sys
sys.path.append("/mnt/c/Users/sneha/Onedrive/Desktop/Oxford/OxComp/PhysicsEssentials/docs")
import basicplot as bp
import numpy as np
import statsmodels.api as sm

class analysis():
    def __init__(self, plot):
        self.plot = plot
    def linreg(self,stats = True):
        x = self.plot.x
        y = self.plot.y
        x = np.reshape(x,(len(x),1)) #Reshaping for Linear Regression
        y = np.reshape(y,(len(y),1)) 
        reg = LinearRegression()
        reg.fit(x,y)
        ypred = reg.predict(x)
        if stats == True:
            xstat = sm.add_constant(x)
            model = sm.OLS(y,xstat).fit()
            print(model.summary())
	    
        return [x,ypred]
    def plotlinreg(self):
        [x, ypred] = self.linreg()
        self.plot.plotscatter(clear = False)
        self.plot.gety(ypred)
        self.plot.getx(x)
        self.plot.plotscatter(clear = True, marker = '--')
"""
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


