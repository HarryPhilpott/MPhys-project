import numpy as np
import matplotlib.pyplot as plt
import math as m
import sympy as sy
from mpmath import *

global co
co = []

def read(fname):
    try:
        lines = [line.rstrip('\n') for line in open(fname)]
    except:
        print 'error opening file ', fname
    return lines

def Sn_function():
    global co
    tot = 0.0
    end = len(co)
    x_range = []
    vals = []

    for i in range(end):
        co[i] = float(co[i])


    ellip = ellipk(co[end-1])
    coeff = -0.5*(co[end-1]**(-0.5))

    length = int(-1000*ellip/coeff) - 1


    
    for x in range(-length,-1):
        for i in range(end-1):
            replace = abs(x)/1000.0
            tot += co[i]*(coeff*replace + ellip)**(1+2*i)
                

        vals.append(m.log(abs(tot)))
        x_range.append(float(x/1000.0))
        tot = 0.0

    vals.append(vals[-1])
    x_range.append(0.0)


    for x in range(1,length):
        for i in range(end-1):
            replace = abs(x)/1000.0
            tot += co[i]*(coeff*replace + ellip)**(1+2*i)

        vals.append(m.log(abs(tot)))
        x_range.append(float(x/1000.0))
        tot = 0.0

    
            

    return np.array(x_range), np.array(vals) 


def graph():
    fig = plt.figure()

    ax = fig.add_subplot(2,2,1)     
    line1, = ax.plot(x1, vals1)
    ax.set_xlabel('X [Debye lengths]')      # k = 0.9
    ax.set_ylabel('Force [N]')
    ax.set_title('k = 0.60')
    

    ax2 = fig.add_subplot(2,2,2)        #k = 0.6
    line2, = ax2.plot(x2,vals2)
    ax2.set_xlabel('X [Debye lengths]')
    ax2.set_ylabel('Force [N]')
    ax2.set_title('k = 0.70')

    ax3 = fig.add_subplot(2,2,3)        #k = 0.7
    line3, = ax3.plot(x3,vals3)
    ax3.set_xlabel('X [Debye lengths]')
    ax3.set_ylabel('Force [N]')
    ax3.set_title('k = 0.80')

    ax4 = fig.add_subplot(2,2,4)        #k = 0.8
    line4, = ax4.plot(x4,vals4)
    ax4.set_xlabel('X [Debye lengths]')
    ax4.set_ylabel('Force [N]')
    ax4.set_title('k = 0.90')



    plt.show()


co = read('coeffs_for_kval__0.6__.txt')
x1, vals1 = Sn_function()

co = read('coeffs_for_kval__0.7__.txt')
x2, vals2 = Sn_function()


co = read('coeffs_for_kval__0.8__.txt')
x3, vals3 = Sn_function()


co = read('coeffs_for_kval__0.9__.txt')
x4, vals4 = Sn_function()




graph()
