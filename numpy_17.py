import matplotlib.pyplot as p
import numpy
x=numpy.array([0, 6, 10, 4, 8])
y=numpy.array([7, 10, 16, 30, 78])
p.plot(x, y)
p.xlabel("time")
p.ylabel("distance")
p.title("Time-Distance graph")
p.grid(axis='x', color='green')
# p.plot(y)
p.show()