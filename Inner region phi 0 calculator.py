import numpy as np
import math as m
import matplotlib.pyplot as plt
import sympy as sy
from mpmath import *

def pot(k, l):

    A = m.sqrt(k)*ellipfun('sn', -l/(2*m.sqrt(k)) + ellipk(k), k)
    print A, k , l


    return A#2*m.log(A)

def phi_zero(phi_s,l):
    res = 0
    i = 0.00001
    counter = 1.0

    while abs(res - phi_s) > 10**(-6):
        res = pot(i,l)
   
        if abs(res) < abs(phi_s):
            i -= 10**(-counter)
            counter += 1.0

        if abs(res) > abs(phi_s):
            i += 10**(-counter)
            

    return -exp(i)

x_range = [0,1,2][:]
phi_nought = [0,1,2][:]

for l in [5]:
    print l
    for i in range(-50, -1):

        x_range.append(i/1000.0)
        phi_nought.append(phi_zero(i/1000.0,l))

        if abs(i)%100 == 0:
            print abs(i)











fig = plt.figure()


ax = fig.add_subplot(1,1,1)
plt.text(-2,0.15,'Mid-Plane Potential Vs Surface Potential For d = 2 Debye lengths')
plt.text(3,-0.15,'Actual Surface Potential [j]')
plt.text(0,-3.1,'Measured Potential [j]')





line1, = ax.plot(x_range[0][:], phi_nought[0][:])
##line2, = ax.plot(x_range, lin_vals, label='Non-Linear Potential')
##line3, = ax.plot(x_range, abs_range, label='Actual Surface Potential')



#ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
#ax.spines['bottom']#.set_position('center')
ax.spines['top'].set_color('black')
ax.spines['left'].set_smart_bounds(False)
ax.spines['bottom'].set_color('none')
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')
ax.grid()
##plt.xlim(-5,5)
##plt.ylim(-3.5,0)
##plt.gca().set_aspect('equal', adjustable='box')
ax.legend(loc=3)

#ax.axes.get_xaxis().set_ticks([0,0.1,0.2,0.3]) #,0.4,0.5,0.6,0.7,0.8,0.9,1.0])



plt.show()
