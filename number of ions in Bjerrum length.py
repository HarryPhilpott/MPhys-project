import matplotlib.pyplot as plt
import math as m
import numpy as np
import sympy as sy
from mpmath import *

def num_co(arg, k, pot):
    exp = m.exp(pot)
    amp = am(arg, k)
    cn = ellipfun('cn', arg, k)
    dn = ellipfun('dn', arg, k)
    sn = ellipfun('sn', arg, k)
    

    term1 = arg

    term2 = ellipe(amp,k)

    term3 = (k**2)*sn*cn/dn


    return (-4.0*(k**(-0.5)))*( term1 - term2 + term3)

def num_counter(arg, k, pot):
    exp = m.exp(pot)
    amp = am(arg, k)
    cn = ellipfun('cn', arg, k)
    dn = ellipfun('dn', arg, k)
    sn = ellipfun('sn', arg, k)

    term1 = arg
    term2 = ellipe(amp,k)
    term3 = sn*dn/cn
    

             
    return (term1 - term2 + term3)*-4.0*(k**(1.5))
    

    
def am(arg,k):
    SN = float(ellipfun('sn', arg, k))
    

    return np.arcsin( SN )


def find_L(potential):

    with open('inter_plate_dist_'+ str(potential) + '.txt', 'r') as f:                    #Function that reads the values of L from a text file.
        pop = f.readlines()

    return pop


coeff = 2.3*(10**-28)
for potential in [2.35]:#, 4.35]:
    L = find_L(potential)
    result = []
    k_range = []
    Lb_range = []
    
    for i in range(100, 1000):              #This finds the integral of charge in the region Xd to L for k values from 0.1 to 1
        print i
        k = i/1000.0
        k_range.append(k)

                
        arg_Lb = float(L[i-100])/10.0#coeff/m.log(k)
        Lb_range.append(arg_Lb)
       

        
        
        term1 = (num_co(arg_Lb, k, potential) - num_co(0.0, k, potential)) #the number of co-ions
        term2 = (num_counter(arg_Lb, k, potential) - num_counter(0.0, k, potential)) #the number of counterions

        
        
        result.append(abs(term1) - abs(term1))
        

        

   
    plt.plot(L, result, label = str(potential))
##    
##plt.xlabel('Inter-Plate Distance [Debye Lengths]')
##plt.ylabel('Charge [e]')
##plt.title('Charge of the dressed macroion for ' + str( (1-error)*100 ) +'% error' )
##plt.legend(loc=0)
plt.grid()
plt.show()












