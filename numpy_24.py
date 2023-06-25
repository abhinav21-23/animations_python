import matplotlib.pyplot as p
import numpy as np
x=np.array(['physics','chemistry','maths','biology','computer'])
y=np.array([20,40,50,60,100])
# p.bar(x,y)  
# p.barh(x,y)
p.bar(x,y, color='red', width=0.2)
p.show()