import sys 
sys.path.append("../../..")
import PhysicsEssentials.docs.dataanalysis as da
import PhysicsEssentials.docs.basicplot as bp
import numpy as np 

x = np.linspace(-10,10,10) 
y = 5*x+3

p1 = bp.plot(x, y, "title", "xlabel", "ylabel")
a1 = da.analysis(p1)
a1.plotlinreg()
