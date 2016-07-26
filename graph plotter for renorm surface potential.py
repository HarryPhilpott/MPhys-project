import numpy as np
import math as m
import matplotlib.pyplot as plt


def results():

    x_range = []
    vals = []
    lin_vals = []
    abs_range = []

    for i in range(-5000, 5000):
        phi = i/1000.0

        abs_range.append(-abs(phi))
        x_range.append(phi)
        vals.append(-4.0*abs(m.tanh(phi/4.0)))
    
        lin_vals.append( 2*(1 - abs( m.tanh(phi/4.0) )) / (1 + abs(m.tanh(phi/4.0))) )
        

    return x_range, vals, lin_vals, abs_range




fig = plt.figure()


ax = fig.add_subplot(1,1,1)
plt.text(-2.5,0.15,'Renormalised linear Surface potential Vs Actual Surface Potential', fontsize='16')
plt.text(2.1,-0.15,'Actual Surface Potential [KbT]', fontsize='16')
plt.text(0,-3.25,'Renormalised linear potential [KbT]', fontsize='16')

x_range, vals, lin_vals, abs_range = results()



line1, = ax.plot(x_range, vals, label='Renormalised linear potential')
#line2, = ax.plot(x_range, lin_vals, label='Non-Linear Potential')
#line3, = ax.plot(x_range, abs_range, label='Actual Surface Potential')



ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
#ax.spines['bottom']#.set_position('center')
ax.spines['top'].set_color('black')
ax.spines['left'].set_smart_bounds(False)
ax.spines['bottom'].set_color('none')
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')
ax.grid()
plt.xlim(-5,5)
plt.ylim(-3.5,0)
##plt.gca().set_aspect('equal', adjustable='box')
#ax.legend(loc=3)

#ax.axes.get_xaxis().set_ticks([0,0.1,0.2,0.3]) #,0.4,0.5,0.6,0.7,0.8,0.9,1.0])



plt.show()
