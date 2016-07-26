import math as m
import numpy as np
import sympy as sy
from mpmath import *
import matplotlib.pyplot as plt
import operator



def exact(k, length):                                 #function returning the value of the exact potential 
    sn = ellipfun('sn')
    ellip = ellipk(k)
    L = find_L(k)
    length = int(1000*length)
    x_range = []
    vals = []
    
    for i in range(-length, length):
        x = i/1000.0
        arg = -0.5*k**(-0.5)*abs(x) + ellip
        x_range.append(x)
        vals.append(2.0*m.log(k**(0.5)*sn(arg,k)))

    return x_range, vals


def lin(k, length):                           #Function returning the value of the linear potential
    L = find_L(k)
    length = int(1000*length)
    coeff = m.log(k)*0.5*m.exp(L)
    vals = []
    x_range = []
    
    for i in range(-length, length):
        x = i/1000.0
        vals.append(coeff*( m.exp(-1.0*abs(x+L)) + m.exp(-1.0*abs(x-L)) ))
        x_range.append(x)

    return x_range, vals

def find_L(k):                      #Function that reads the values of L from a text file.

    with open('inter_plate_dist_2.35.txt', 'r') as f:                    
        pop = f.readlines()



    return float(pop[int(1000*k)-100])

length = float(find_L(m.exp(-1.1)))
x, vals = exact(m.exp(-1.1), length)
x, vals2 = lin(m.exp(-1.1), length)



fig = plt.figure()
fig.suptitle('Linear and Non-Linear plots', fontsize = 16)


ax = fig.add_subplot(2,2,1)     
#line1, = ax.plot(x, map(operator.sub, vals, vals2), label = 'exact solution')
line1, = ax.plot(x, vals, label = 'exact solution', linestyle='-.')
line1, = ax.plot(x, vals2, label = 'linear solution')
ax.set_xlabel('X [Debye lengths]', fontsize = 12)      # k = 0.9
ax.set_ylabel('Potential [KbT]', fontsize = 16)
ax.set_title('Inter-plate distance = ' + str(length) + '[Debye-Lengths]', fontsize = 16)
ax.legend(loc=8)
ax.grid()

length = find_L(m.exp(-1.15))
x, vals = exact(m.exp(-1.15), length)
x, vals2 = lin(m.exp(-1.15), length)

ax2 = fig.add_subplot(2,2,2)        #k = 0.6
#line2, = ax2.plot(x, map(operator.sub, vals, vals2), label = 'exact solution')
line1, = ax2.plot(x, vals, label = 'exact solution', linestyle='-.')
line1, = ax2.plot(x, vals2, label = 'linear solution')
ax2.set_xlabel('X [Debye lengths]', fontsize = 12)
ax2.set_ylabel('Potential [KbT]', fontsize = 16)
ax2.set_title('Inter-plate distance = ' + str(length) + '[Debye-Lengths]', fontsize = 16)
ax2.legend(loc=8)
ax2.grid()

length = find_L(m.exp(-1.20))
x, vals = exact(m.exp(-1.20), length)
x, vals2 = lin(m.exp(-1.20), length)

ax3 = fig.add_subplot(2,2,3)        #k = 0.7
#line2, = ax3.plot(x,map(operator.sub, vals, vals2), label = 'exact solution')
line1, = ax3.plot(x, vals, label = 'exact solution', linestyle='-.')
line1, = ax3.plot(x, vals2, label = 'linear solution')
ax3.set_xlabel('X [Debye lengths]', fontsize = 16)
ax3.set_ylabel('Potential [KbT]', fontsize = 16)
ax3.set_title('Inter-plate distance = ' + str(length) + '[Debye-Lengths]', fontsize = 15)
ax3.legend(loc=8)
ax3.grid()

length = find_L(m.exp(-1.25))
x, vals = exact(m.exp(-1.25), length)
x, vals2 = lin(m.exp(-1.25), length)

ax4 = fig.add_subplot(2,2,4)        #k = 0.8
#line2, = ax4.plot(x,map(operator.sub, vals, vals2), label = 'exact solution')
line1, = ax4.plot(x, vals, label = 'exact solution', linestyle='-.')
line1, = ax4.plot(x, vals2, label = 'linear solution')
ax4.set_xlabel('X [Debye lengths]', fontsize = 16)
ax4.set_ylabel('Potential [KbT]', fontsize = 16)
ax4.set_title('Inter-plate distance = ' + str(length) + '[Debye-Lengths]', fontsize = 15)
ax4.legend(loc=8)
ax4.grid()


plt.show()



                  
