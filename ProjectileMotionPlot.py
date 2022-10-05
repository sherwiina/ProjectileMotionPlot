import matplotlib.pyplot as plt
from numpy import arange
from math import pi,tan,cos,sin
angle = 30
g = 9.8
v0 = 20
y = 0
x = 0
plt.plot(x,y,"ko")
for t in arange (0,20,0.1) :
   x = x + v0*cos(angle*pi/180)*t
   y = y + v0 * sin(angle * pi / 180) - 0.5 * g * (t**2)
   plt.plot(x,y,"ko")
plt.show()

