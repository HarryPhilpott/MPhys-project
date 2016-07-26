import numpy as np
import scipy as sci
import math
import matplotlib.pyplot as plt

def sinc_calc(r, d, dmin):
    c = np.pi/(2.0*r)
    sum1 = 0.0
    A = math.cos(c*dmin)
    for i in range(1,15):

        sum1 += ((c**(2*i-1))*(d**(2*i-1))*(-1)**(i+1))/(((2*i-1)**2)*sci.math.factorial(2*i-2))

    return A*sum1


def cosc_calc(r, d, dmin):
    c = np.pi/(2.0*r)
    sum1 = 0.0
    B = math.sin(c*dmin)
    for i in range(1,15):
        sum1 += (c**(2*i))*(d**(2*i))*((-1)**i)/(2*i*sci.math.factorial(2*i))

    return B*(sci.log(d) + sum1)

data = []

for i in range(40):
    data.append((sinc_calc(0.1, i*0.01+0.2, i*0.10) - sinc_calc(0.1, i*0.01, i*0.01) - cosc_calc(0.1, i*0.01+0.2, i*0.01) + cosc_calc(0.1, i*0.01, i*0.1)))
        

plt.plot(np.arange(0,40), data)
plt.show()
