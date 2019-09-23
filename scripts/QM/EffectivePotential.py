import sys 
sys.path.append("../../..") 
import PhysicsEssentials.docs.basicplot as bp 
import numpy as np 
from optparse import OptionParser 
"""
Optional Parsing
"""
parser = OptionParser()
parser.add_option("--Vexp", type = "int", help = "Exponent of Potential", dest = "a", default = 0)
parser.add_option("--title", type = "string", help = "Title of graph", dest = "title", default = "Constant")
parser.add_option("--l", type = "int", help = "Value of l", dest = "l", default = 1)
parser.add_option("--save", help = "Do you want to save the graph", dest = "save", default = True)
options, arguments = parser.parse_args()

a = options.a 
title = options.title
l = options.l
save = options.save
"""
Rest of the Program
"""

r = np.linspace(0, 10, 100) 
#a = 2
V = r**a 


Veff = lambda r: V + (l*(l+1))/(r**2)
p1 = bp.plot(r, Veff(r), "Effective Potential: " + title, 'r', 'Veff (l = '+str(l) + ' )')
p1.plotscatter(marker ='--', save = save, impath = "EffectivePotential/"+title+".png") 

#print("EffectivePotential/"+title.split()[-1]+".png")
