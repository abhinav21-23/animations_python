import matplotlib.pyplot as p
import numpy as np
x=np.array([2,4,6,7,8])
y=np.array([3,45,1,5,6])
color=np.array(['green','blue','black','pink','orange'])
p.scatter(x,y,c=color)
p.show()