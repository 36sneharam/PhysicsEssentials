import basicplot
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# y = 1 * x_0 + 2 * x_1 + 3
x = np.random.randn(10,1)
y = 2*x+3+0.1*np.random.randn(10,1)
plt.scatter(x,y)
model = LinearRegression()
model.fit(x,y)
y_pred = model.predict(x) 
plt.plot(x,y_pred)
plt.show()

x = np.linspace(0,10,10) 
x = np.reshape(x,(len(x),1)) 
print(np.shape(x))
print(x)
