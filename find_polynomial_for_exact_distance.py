"""The purpose of this program is to help find the exact function that gives the distance from the plate
for a given error. It intends to do this by finding the coefficients of the polynomial that is nested in
a larger function"""


import math as m
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

global k


def approx_function(k):
    coeff = 1.0 - m.sqrt(1-k**2 + k**3)
    poly = 0.0

    


#    for i in range(1,30):
#        poly += coeff*(-k**(i+1))**i
        
    poly = m.sqrt(1-k)/k
 
   # try:
    


    return m.log(2.0*m.cosh(poly))/(k*m.tanh(poly)) #abs(1-term1/term2)
##    except:
##        return 0.101010101
##        pass




sum2 = 0.0



for i in range(1,99):
    k = i/100.0
    res = approx_function(k)
    print  res
    sum2+= res

print ''
print ''
print sum2
    
    


