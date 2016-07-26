import math as m
import matplotlib.pyplot as plt

x_range = []
res = []



for i in range(1,1000):
    x  = i/1000.0
    res.append( (-2.0*m.sqrt(1-x) ) / ( m.log( (1 - m.sqrt(1-x))/(1+m.sqrt(1-x)))))
    x_range.append(x)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(x_range, res)
plt.xlabel('Error in the Force')
plt.ylabel('Error in the Potential')
plt.title('Error in the Potential Vs Error in the Force at the edge of the Dressed Macroion')
ax.set_xticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax.set_ylim(bottom=0.0, top=1.0)
ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.grid()
plt.show()
