import math as m
import numpy as np
import sympy as sy
from mpmath import *
import matplotlib.pyplot as plt

def exact(k,x, L):                                 #function returning the value of the exact potential 
    arg = -0.5*k**(-0.5)*abs(x) + ellipk(k)
    sn = ellipfun('sn')


    return 2.0*m.log(k**(0.5)*sn(arg,k))


def lin(k,x,L):
    coeff = m.log(k)*0.5*m.exp(L)
                                                                        #Function returning the value of the linear potential
    return coeff*( m.exp(-1.0*abs(x+L)) + m.exp(-1.0*abs(x-L)) )

def find_L(k):

    with open('inter_plate_dist.txt', 'r') as f:                    #Function that reads the values of L from a text file.
        pop = f.readlines()



    return float(pop[int(100*k)-10])

def write(string, error):
        
    with open('x_vals_for_error_'+str(error)+'__.txt', 'a') as f:
        f.write(string + '\n')                                          #Subroutine that writes strings to a text file.
        f.close()


def find_dist(k, error):
    L = find_L(k)
    x = L
    lin_res = lin(k,x,L)
    ex_res = exact(k,x,L)

    ratio = ex_res/lin_res
                                                                #Main function that calculates the ratio of the exact value to the linear value.
                                                                #If the value is greater than a specified value the value of distance is returned.

    print ''
    print k
    print ''
    
    while ratio < error and x > 0:
        #print abs(ratio), '      ', error
        x -= 1/1000.0

        lin_res = lin(k,x,L)
        ex_res = exact(k,x, L)

        ratio = ex_res/lin_res

    print 'x = ',x,' L = ',L , '  error = ',  error, '  ratio = ', ratio
    return x



##for i in range(96,1000):            #below 96 the mid plane potential is larger than the surface potential
##    
##    res = find_dist(i/1000.0,0.99)
##    write(str(res),0.99)

for i in range(10,100):            #below 96 the mid plane potential is larger than the surface potential
    
    res = find_dist(i/100.0,0.9)
#    write(str(res),0.5)
#    print i



for i in range(10,100):            #below 96 the mid plane potential is larger than the surface potential
    
    res = find_dist(i/100.0,0.1)
 #   write(str(res),0.1)
#    print i
