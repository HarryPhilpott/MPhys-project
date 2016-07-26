import math as m
from scipy import integrate
import matplotlib.pyplot as pl
from scipy.optimize import curve_fit
import numpy as np

def func(x,a,b,c,d):
    result = a + b*np.cos(x)*np.sqrt(d+c*np.cos(x))
    return result
   

integrand = lambda x: float((m.sin(x)*(1-d*m.cos(x)))/m.sqrt(1+d**2-2*d*m.cos(x)))


result = []
x_range = []
d = 1

for i in range(1,100):
    d = i
    x_range.append(float(i))
    flop, error = integrate.quad(integrand, 0 ,m.pi)
    result.append(float(flop))

popt, pcov = curve_fit(func, x_range, result)

print popt
print ' '
print pcov
    
