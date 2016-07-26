'''starting from x = previous value - 0.1, to imporve speed'''

import math as m
import numpy as np
import sympy as sy
from mpmath import *


def exact(x):                                 #function returning the value of the exact potential 
    

    return 2.0*m.log(k**(0.5)*sn(arg,k))


def lin(x):
    
                                                                        #Function returning the value of the linear potential
    return coeff*( m.exp(-1.0*abs(x+L[pos])) + m.exp(-1.0*abs(x-L[pos])) )



def find_L(potential):

    with open('inter_plate_dist_'+ str(potential) + '.txt', 'r') as f:                    #Function that reads the values of L from a text file.
        pop = f.readlines()

    return pop



def write(string, error, potential):
        
    with open('x_vals_for_error_'+str(error)+'_potential_2'+ str(potential) + '.txt', 'a') as f:
        f.write(string + '\n')                                          #Subroutine that writes strings to a text file.
        f.close()



def find_dist(k, error, previous, length):
    x = 0.0
    
    pos = int(1000*k) - 100
    coeff = m.log(k)*0.5*m.exp(L[pos])

    ellip = ellipk(k)
    ex_coeff = -0.5*k**(-0.5)
    ex_coeff2 = k**(0.5)
    sn = ellipfun('sn')
    
##    if previous > 0.3:
##        x = previous - 0.3
##    else: x = 0.0

                                                                #Main function that calculates the ratio of the exact value to the linear value.
                                                                #If the value is greater than a specified value the value of distance is returned.
    ratio = 1.0


    while abs(1-ratio) < 1-error and x < length:
        x += 1/1000.0
        arg = ex_coeff*abs(x) + ellip
        lin_res = coeff*( m.exp(-1.0*abs(x+L[pos])) + m.exp(-1.0*abs(x-L[pos])) )
        ex_res = 2.0*m.log(ex_coeff2*sn(arg,k))

        ratio = ex_res/lin_res

    
    
    return x

res = 0.0
global L


for potential in [2.35, 4.35]:
    L = find_L(potential)
    L = [float(i) for i in L]               
    for error in [0.9, 0.99,0.999]:
        for i in range(100,1000):            #below 10 the mid plane potential is larger than the surface potential
            k = i/1000.0
            
            res = find_dist( k, error, res, L[i - 100] )
            write(str(res),error,potential)
            print i
            
        print ''
        print ''
        res = 0.0

