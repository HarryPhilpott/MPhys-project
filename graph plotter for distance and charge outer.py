import numpy as np
import math as m
import matplotlib.pyplot as plt


#This is incomplete !!! I need to account for kappa change

def dist_calc(err, charge):
    interior = abs(m.tanh(charge/4))*(1-err)**(-0.5)

    

    return m.log(interior)

def produce_results(err):

    results = []
    x_range = []



    for i in range(-5000,5000):
        charge = i/1000.0
        
        if charge != 0.0:
            x_range.append(charge)
            pop = dist_calc(err, charge)
            results.append(pop)
            
                
            

    return x_range, results




fig = plt.figure()


ax = fig.add_subplot(1,1,1)
ax.set_title('Acceptable Distance Vs Surface Potential', fontsize='16')
plt.text(1.8,-0.9,'Surface Potential [KbT]', fontsize='16')
plt.text(0,3.5,'Acceptable Distance [Debye Lengths]', fontsize='16')

line1, = ax.plot(produce_results(0.999)[0], produce_results(0.999)[1],label='gottlob', linestyle='--')
line1.set_label('0.1% Error')

line2, = ax.plot(produce_results(0.99)[0], produce_results(0.99)[1],label='gottlob', linestyle='-.')
line2.set_label('1% Error')

line3, = ax.plot(produce_results(0.9)[0], produce_results(0.9)[1],label='gottlob')
line3.set_label('10% Error')

ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.grid()
plt.xlim(-5,5)
plt.ylim(-4,4)
plt.gca().set_aspect('equal', adjustable='box')
ax.legend(loc=4, fontsize='16')

ax.axes.get_xaxis().set_ticks([-5,-4,-3,-2,-1,1,2,3,4,5])

plt.show()
