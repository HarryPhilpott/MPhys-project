import numpy as np
import matplotlib.pyplot as plt
import math as m

global co
co = []

def read(fname):
    try:
        lines = [line.rstrip('\n') for line in open(fname)]
    except:
        print 'error opening file ', fname
    return lines

def Sn_function(trunc):
    global co
    tot = 0.0
    length = 1500
    x_range = []
    vals = []    
    
    for x in range(-length,length):
        for i in range(trunc):
            if x == 0:
                tot += float(float(co[i])*(abs(x-1)/1000.0)**(i))
            else:
                tot += float(float(co[i])*(abs(x)/1000.0)**(i))
                

        vals.append(2*m.log(abs(tot)) + m.log(0.1))
        x_range.append(float(x/1000.0))
        tot = 0.0
            

    return np.array(x_range), np.array(vals) 


def graph():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x_range, vals = Sn_function(10)
    x_range2, vals2 = Sn_function(8)
    x_range3, vals3 = Sn_function(5)
    x_range4, vals4 = Sn_function(3)
    line1, = ax.plot(x_range, vals, label = '9')
    line2, = ax.plot(x_range2, vals2, label = '7')
    line3, = ax.plot(x_range3, vals3, label = '4')
    line4, = ax.plot(x_range4, vals4, label = '2')
    plt.title('potential in the inner region of a k = 0.1 system, using truncated formulas of Sn')
    ax.set_xlabel('X [Debye lengths]')
    ax.set_ylabel('Potential [J]')

##    ax.spines['left'].set_position('center')
##    ax.spines['right'].set_color('none')
##    ax.spines['bottom']#.set_position('center')
##    ax.spines['top'].set_color('black')
##    ax.spines['left'].set_smart_bounds(False)
##    ax.spines['bottom'].set_color('none')
##    ax.xaxis.set_ticks_position('top')
##    ax.yaxis.set_ticks_position('left')
##    ax.grid()
##    plt.xlim(-0.8,0.8)
##    plt.ylim(-3.5,0)
##    plt.gca().set_aspect('equal', adjustable='box')
    ax.legend(loc=3)
    

    #ax.axes.get_xaxis().set_ticks([0,0.1,0.2,0.3]) #,0.4,0.5,0.6,0.7,0.8,0.9,1.0])



    plt.show()

co = read('coeffs_for_kval__0.1__.txt')





graph()
