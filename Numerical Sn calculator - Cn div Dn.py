import math as m
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
from mpmath import *


def write(string):
        
    with open('Inter_plate_dist.txt', 'a') as f:
        f.write(string + '\n')
        f.close()
        




def Cn_coeff_1():
    return -0.5

def Cn_coeff_2(k):
    return (1.0+4.0*k**2.0)/m.factorial(4.0)

def Cn_coeff_3(k):
    return -1.0*(1+44.0*k**2 + 16.0*k**4)/m.factorial(6.0)



def Dn_coeff_1(k):
    return -0.5*k**2

def Dn_coeff_2(k):
    return (4*k**2 + k**4)/m.factorial(4.0)

def Dn_coeff_3(k):
    return -1.0*(16.0*k**2 + 44.0*k**4 + k**6)/m.factorial(6.0)



def graph():
    fig = plt.figure()
    k_vals = [0.1+0.2*i for i in range(5)]
    

    ax = fig.add_subplot(2,2,1)
    x1, vals1 = Sn_function(k_vals[0],1)
    line1, = ax.plot(x1, vals1)
    ax.set_xlabel('X [Debye lengths]')      
    ax.set_ylabel('Potential [j]')
    ax.set_title('k = '+ str(k_vals[0]))
    

    x2, vals2 = Sn_function(k_vals[1],1)
    ax2 = fig.add_subplot(2,2,2)
    line2, = ax2.plot(x2, vals2)
    ax2.set_xlabel('X [Debye lengths]')
    ax2.set_ylabel('Potential [j]')
    ax2.set_title('k = '+ str(k_vals[1]))

    
    x3, vals3 = Sn_function(k_vals[2],1)
    ax3 = fig.add_subplot(2,2,3)
    line3, = ax3.plot(x3,vals3)
    ax3.set_xlabel('X [Debye lengths]')
    ax3.set_ylabel('Potential [j]')
    ax3.set_title('k = '+ str(k_vals[2]))


    x4, vals4 = Sn_function(k_vals[3],1)
    ax4 = fig.add_subplot(2,2,4)
    line4, = ax4.plot(x4,vals4)
    ax4.set_xlabel('X [Debye lengths]')
    ax4.set_ylabel('Potential [j]')
    ax4.set_title('k = '+ str(k_vals[3]))



    plt.show()


    
        
def Sn_function(k_val, choice):
    co = []
    vals = []
    Dn_co = []
    Cn_co = []
    x_range = []
    L = 0.0
    
    switch = 0

    
    ellip = ellipk(k_val)
    coeff = -0.5*(k_val**(-0.5))

    Dn_co.append(1.0)
    Dn_co.append(Dn_coeff_1(k_val))
    Dn_co.append(Dn_coeff_2(k_val))
    Dn_co.append(Dn_coeff_3(k_val))

    Cn_co.append(1.0)
    Cn_co.append(Cn_coeff_1())
    Cn_co.append(Cn_coeff_2(k_val))
    Cn_co.append(Cn_coeff_3(k_val))

    length = int(-1000*ellip/coeff) - 1
#    length = 1900


    for i in range(-length,-1):
        x = float(coeff*i/1000.0)

        Dn = Dn_co[0] + Dn_co[1]*x**2 + Dn_co[2]*x**4 + Dn_co[3]*x**6

        Cn = Cn_co[0] + Cn_co[1]*x**2 + Cn_co[2]*x**4 + Cn_co[3]*x**6
            
        vals.append(2*m.log(abs(Cn/Dn))) #+ m.log(k_val))
        x_range.append(i/1000.0)

        
        if abs(2*m.log(abs(Cn/Dn)) + m.log(k_val)) < 2.35 and switch == 0:
            switch = 1
            L = abs(2*i/1000.0)



    vals.append(vals[-1])
    x_range.append(0.0)
    

    for i in range(2,length - 1):
        vals.append(vals[-2*i])
        x_range.append(-1.0*x_range[-2*i])


    if choice == 1:
        return np.array(x_range), np.array(vals)
    else:
        return L

#graph()
L = []
x = []

for i in range(11,100):
    x.append(i/100.0)
    L.append(Sn_function(i/100.0,0))
    write(str(Sn_function(i/100.0,0)))

plt.figure()

plt.plot(x, L)
plt.show()




##def exponential_function(k_val):
##    coeff = 0.5*m.log(k_val)*m.exp(1.5)
##    vals = []
##    x_range = []
##
##    
##    
##
##    length = 1400
##    
##
##    for i in range(-length,-1):
##        x = i/1000.0
##
##        vals.append( coeff*( m.exp(-abs(x+1.5)) + m.exp( -abs(x-1.5))) )
##        x_range.append(x)
##
##    vals.append(vals[-1])
##    x_range.append(0.0)
##
##    for i in range(2,length - 1):
##        vals.append(vals[-2*i])
##        x_range.append(-1.0*x_range[-2*i])
##
##    return np.array(x_range), np.array(vals)
