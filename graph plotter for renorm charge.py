import numpy as np
import math as m
import matplotlib.pyplot as plt

def err_func(err):
    top = 1 + (1-err)**(1/8.0)
    bottom = 1 - (1-err)**(1/8.0)

    return (top/bottom)**2 + (bottom/top)**2


def renorm_charge(err):
    n0 = 10**19
    e = 1.6*10**-19
    E0 = 8.85*10**-12
    Kb = 1.38*10**-23
    T = 273.0

    Hp = m.sqrt((2*E0*Kb)/(m.pi*e**2))
    
    results = []
    x_range = []
    
    err_value = err_func(err)

    for i in range(-5000, 5000):
        if i != 0:
            phi = i/1000.0
            x_range.append(phi)
            polarity = phi/abs(phi)

            hyp = m.cosh(phi/2.0)**2 + m.cosh(phi/2.0)**-2 - Hp*m.sqrt(T/n0)*(polarity**-1)*m.sinh(phi/2.0)

            results.append(n0*e*polarity*(err_value - hyp))

    return x_range, results






fig = plt.figure()


ax = fig.add_subplot(1,1,1)
ax.set_title('Charge of Dressed macroion Vs Surface Potential at Different Values of error at n0 = 10^19 m^-3 and T = 273K', fontsize = 16)
plt.text(5,-0.9,'Surface Potential [j]', fontsize = 16)
plt.text(-1,67,'Charge [c]', fontsize = 16)



line1, = ax.plot(renorm_charge(0.99)[0], renorm_charge(0.99)[1],label='gottlob')
line1.set_label('Error = 1%')

line2, = ax.plot(renorm_charge(0.999)[0], renorm_charge(0.999)[1],label='gottlob')
line2.set_label('Error = 0.1%')

line3, = ax.plot(renorm_charge(0.9)[0], renorm_charge(0.9)[1],label='gottlob')
line3.set_label('Error = 10%')

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
ax.legend(loc=3, fontsize = 16)

ax.axes.get_xaxis().set_ticks([-5,-4,-3,-2,-1,1,2,3,4,5])



plt.show()










##line1, = ax.plot(results(0.9, 10**30)[0], results(1, 10**30)[1],label='gottlob')
##line1.set_label('n0 = 10**9')
##
##line2, = ax.plot(results(1, 10**8)[0], results(1, 10**8)[1],label='gottlob')
##line2.set_label('n0 = 10**8')
##
##line3, = ax.plot(results(1, 10**7)[0], results(1, 10**7)[1],label='gottlob')
##line3.set_label('n0 = 10**7')
##
##line3, = ax.plot(results(1, 10**6)[0], results(1, 10**6)[1],label='gottlob')
##line3.set_label('n0 = 10**6')
