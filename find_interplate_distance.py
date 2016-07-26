import math as m
import numpy as np
import sympy as sy
from mpmath import *


def exact(k,x):
    arg = -0.5*k**(-0.5)*abs(x) + ellipk(k)                        #Function returning the exact value of potential at point x and value k
    sn = ellipfun('sn')


    return 2.0*m.log(k**(0.5)*sn(arg,k))

def write(string, potential):
        
    with open('inter_plate_dist_' + str(potential) + '.txt', 'a') as f:        #subroutine that writes text to file
        f.write(string + '\n')
        f.close()

        
x = 0.0
potential = 4.35

for i in range(100,1000):
    res = abs(exact(i/1000.0, x))                    #looping over i increments the k value

    while res < potential:                               # loops until the potential at point x is greater than 2.35 
        x += 1/1000.0                               # (which is an arbitrary surface potential that was chosen)
        res = abs(exact(i/1000.0, x))

    write(str(x),potential)
    
