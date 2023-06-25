import matplotlib.pyplot as p
import numpy as np
x=np.array([2,4,6,7,8,9,10,23,54,6,7,83,2,67,100])
y=np.array([3,45,1,5,6,78,9,2,3,45,8,2,7,9,54])
p.scatter(x,y, color='green')
x1=np.array([33,55,2,1,5,68,94])
y1=np.array([3,45,1,5,6,78,9])
p.scatter(x1,y1, color='red')
p.show()