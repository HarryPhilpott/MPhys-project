import numpy as np
import math as m
import matplotlib.pyplot as plt



def results():
    x_range = []
    vals = []

    for i in range(1,1000):
        err = i/1000.0
        x_range.append(err)

        top = -2.0*m.sqrt(1.0-err)
        bottom = m.log(1.0-m.sqrt(1.0-err)) - m.log(1.0 + m.sqrt(1.0-err))
        vals.append(top/bottom)

    return x_range, vals








fig = plt.figure()


ax = fig.add_subplot(1,1,1)
ax.set_title('True error at Xd Vs simple error')
plt.text(0.5,-0.05,'Simple Error')
plt.text(0,1.05,'True Error')



line1, = ax.plot(results()[0], results()[1])


##ax.spines['left'].set_position('center')
##ax.spines['right'].set_color('none')
##ax.spines['bottom'].set_position('center')
##ax.spines['top'].set_color('none')
##ax.spines['left'].set_smart_bounds(False)
##ax.spines['bottom'].set_smart_bounds(True)
##ax.xaxis.set_ticks_position('bottom')
##ax.yaxis.set_ticks_position('left')
ax.grid()
##plt.xlim(-5,5)
plt.ylim(-0.002,1)
##plt.gca().set_aspect('equal', adjustable='box')
ax.legend(loc=3)

ax.axes.get_yaxis().set_ticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
ax.axes.get_xaxis().set_ticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])



plt.show()
