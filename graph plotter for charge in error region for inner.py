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

def read(error, potential):

    with open('x_vals_for_error_'+str(error)+'_potential_' + str(potential) + '.txt', 'r') as f:
        results = f.readlines()

    return results
    

    
def am(arg,k):
    SN = float(ellipfun('sn', arg, k))
    

    return np.arcsin( SN )

def find_L(potential):

    with open('inter_plate_dist_'+ str(potential) + '.txt', 'r') as f:                    #Function that reads the values of L from a text file.
        pop = f.readlines()

    return pop

error  = 0.999


start = 100
end = 1000

potential_list = [2.35, 4.35]

for potential in potential_list:
    distance = read(error, potential)
    L = find_L(potential)
    result = []
    
    
    for i in range(start, end):              #This finds the integral of charge in the region Xd to L for k values from 0.1 to 1
        print i
        k = i/1000.0
        coeff = -0.5*k**(-0.5)
                
        arg_Xd = coeff*float(distance[i -100])
       

        
        
        term1 = (num_co(arg_Xd, k, potential) - num_co(0.0, k, potential)) #the number of co-ions
        term2 = (num_counter(arg_Xd, k, potential) - num_counter(0.0, k, potential)) #the number of counterions

        
        
        result.append((abs(term2) - abs(term1)))
        

        

    if potential == 4.35: 
        plt.plot(L[(start-100):(end-100)], result, label = 'Surface potential = ' + str(potential), linestyle = '-.')
    else:
        plt.plot(L[(start-100):(end-100)], result, label = 'Surface potential = ' + str(potential))
    
plt.xlabel('Inter-Plate Distance [Debye Lengths]', fontsize = 16)
plt.ylabel('Charge [e]', fontsize = 16)
plt.title('Charge of the dressed macroion for ' + str( (1-error)*100 ) +'% error', fontsize = 16)
plt.legend(loc=0, fontsize = 16)
plt.grid()
plt.show()












