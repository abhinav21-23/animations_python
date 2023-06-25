import matplotlib.pyplot as p
import numpy as np
x=np.array([12,20,34,40,50])
l=["abhi", "shrey", "mukul", "binay", "jha"]
c=['green', 'blue', 'black', 'red', 'purple']
a=[0,0,0.4,0,0]
p.pie(x, labels=l, colors=c)
p.show()