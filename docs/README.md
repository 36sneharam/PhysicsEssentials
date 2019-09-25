# DOCS
This directory has the following modules each covering different physics applications:

 1. basicplot.py
 2. dataanalysis.py 
 3. coordtrans.py 

## basicplot
Base module for plotting different kinds of graphs
```python
Class PhysicsEssentials.basicplot.plot
```
**Methods**
```python
__init__(self, x, y, **kwargs)
```
Parameters: 
1. Required   
**x (array) :** data for x coordinates of points on plot   
**y (array) :** data for y coordinates of points on plot  
2. Optional  
**title (string) :** title of plot. Default: "title"  
**xaxis (string) :** label of xaxis. Default: "xaxis"  
**yaxis (string) :** label of yaxis. Default: "yaxis"  
**coord (string) :** type of coordinate system ["Cart", "Polar"]. Default: "Cart"
    
```python
getx(self, x)
```
Parameters:  
**x (array) :** re-assigned x coordinates of plot 

```python
gety(self, y)
```
Parameters:  
**x (array) :** re-assigned y coordinates of plot 

```python
plotscatter(self, **kwargs)
```
Parameters:  
1. Required  
**save (bool) :** parameter that indicates if figure should be saved. Default: False   
**impath (string) :** path to save the plot   
**marker (string) :** marker for scatter plot points (Matplotlib options). Default: 'o'
**clear (bool) :** parameter that indicates if figure should be cleared before next plot. Default: True

```python
plot3D(self, z, **kwargs) 
```
Parameters:  
1. Required  
**z (array or lambda) :** z coordinates of plot. Is lambda for wireframe and surface and array for scatter and line
2. Options  
**zaxis (string) :** label of z axis. Default: "zaxis"  
**type (string) :** type of 3D plot ["scatter", "line", "wireframe", "surface"]. Default: "line"  

```python
getvectorfield(self, vfield) 
```
Parameters:  
1. Required  
**vfield (lambda) :** vector field to be assigned to plot (self)

```python
plotvectorfield(self, **kwargs) 
```
Parameters:  
2. Options  
**save (bool) :** parameter that indicates if figure should be saved. Default: False   
**impath (string) :** path to save the plot     
NOTE: Use getvectorfield(self, vfield) before using this function

## data analysis

Base module for performing data analysis on graph like regressions etc. 

```python
Class PhysicsEssentials.dataanalysis.analysis
```
**Methods**
```python
__init__(self, plot)
```
Parameters: 
1. Required   
**plot (plot from PhysicsEssentials.basicplot.plot) :** plot to be analysed

```python
linreg(self, **kwargs)
```
Parameters:   
Optional
1. **stats (bool) :** should statistics of the regression be displayed. Default: True
    
Return:  
[x, ypred] : x and y coordinates of linear fit 

```python
plotlinreg(self)

```
NOTE: this function plots the linear regression fit and the original scatter plot

