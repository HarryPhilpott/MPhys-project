import matplotlib.pyplot as plt
import math as m
import numpy as np

lin = []
exact = []

t = m.log( abs(1.0/(m.tanh(-2.35/4.0))))
phi_r = -2.35 #-4.0*abs( m.tanh(-2.35/4.0) )

for i in range(-1000,1000):
    x = abs(i/1000.0)

    exact.append( 2.0*m.log( m.tanh(0.5*(x+t))))
    lin.append( phi_r*m.exp(-x) )

x_range = [i/1000.0 for i in range(-1000,1000)]


fig = plt.figure()


ax = fig.add_subplot(1,1,1)
#ax.set_title('Linear and Exact Potentials in the Outer Region')
plt.text(-0.45, -0.5, 'Linear potential and Exact Potentials in the Outer Region', fontsize='16')
plt.text(-0.2,-2.4,'Potential [KbT]', fontsize='16')
plt.text(0.2,-0.7,'Distance from the Plate [Debye Lengths]', fontsize='16')



line1, = ax.plot(x_range, lin, linestyle='--')
line1.set_label('Linear Potential')

line2, = ax.plot(x_range, exact)
line2.set_label('Exact Potential')

ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('top')
ax.spines['bottom'].set_color('none')
#ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')
ax.grid()


ax.legend(loc=3, fontsize='16')
plt.show()

