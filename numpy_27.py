import matplotlib.pyplot as p
import numpy as np
x=np.array([2,4,6,7,8])
y=np.array([3,45,1,5,6])
color=np.array([1,2,3,4,5])
size=np.array([1000,3000,10000,15000,20000])
p.scatter(x,y,c=color, cmap='viridis', s=size, alpha=0.5)
p.show()