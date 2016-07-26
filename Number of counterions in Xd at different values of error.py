import numpy as np
import math as m
import matplotlib.pyplot as plt

def err_func(err):
    top = 1 + (1-err)**(1/8.0)
    bottom = 1 - (1-err)**(1/8.0)

    return (top/bottom)**2

def num_counter(err):

    x_range = []
    results = []
    
    for i in range(-5000, 5000):

        if i!= 0:
            phi = i/1000.0
            x_range.append(phi)

            

            results.append((-m.cosh(phi/2)**-2 + (err_func(err))))


    return x_range, results



fig = plt.figure()


ax = fig.add_subplot(1,1,1)
ax.set_title('Number of Coions in range Xd Vs Surface Potential at Different Values of error')
plt.text(5,-0.9,'Surface Potential [j]')
plt.text(-1,67,'Number of Counterions [n0]')



line1, = ax.plot(num_counter(0.99)[0], num_counter(0.99)[1],label='gottlob')
line1.set_label('Error = 1%')

line2, = ax.plot(num_counter(0.999)[0], num_counter(0.999)[1],label='gottlob')
line2.set_label('Error = 0.1%')

line3, = ax.plot(num_counter(1)[0], num_counter(1)[1],label='gottlob')
line3.set_label('Error = 0%')

ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.grid()
##plt.xlim(-5,5)
##plt.ylim(-4,4)
##plt.gca().set_aspect('equal', adjustable='box')
ax.legend(loc=3)

ax.axes.get_xaxis().set_ticks([-5,-4,-3,-2,-1,1,2,3,4,5])



plt.show()
