import scipy
from scipy import integrate, optimize
import math
import numpy as np
import matplotlib.pyplot as plt


pi = scipy.pi
sinc = lambda x: pi*math.sin(pi*(x - dmin)/(2*r))/(2*r*x)
data = []

x = np.arange(0.1,10,0.01)
for i in x:
    dmin = i
    r = 0.1

    result, err = scipy.integrate.quad(sinc, dmin, dmin+r)

    data.append(result)



def curve(x,a, b, c, d, e):
    return (b*scipy.exp(-d*x))/(e*scipy.tanh(a*x)) + c

opt, pcov = scipy.optimize.curve_fit(curve, x, data)

print np.average(abs(data - curve(x,opt[0], opt[1], opt[2], opt[3], opt[4]))), np.std(abs(data - curve(x,opt[0], opt[1], opt[2], opt[3], opt[4])))

plt.plot(x, data, 'r')
plt.plot(x, curve(x,opt[0], opt[1], opt[2], opt[3], opt[4]))
plt.show()
