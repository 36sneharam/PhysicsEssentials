import numpy as np 
import matplotlib.pyplot as plt 

class plot:
    def __init__(self, x, y, title):
        self.x = x 
        self.y = y 
        self.title = title 
    def myplot(self): 
        plt.plot(self.x,self.y,'o')
        plt.title(self.title)
        
        plt.show()
    
    
p1 = plot([1,2,3], [2,3,5], "Title") 
p1.myplot()

