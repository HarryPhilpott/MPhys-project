import math as m
import pylab as pl
import numpy as np

def sinc(num_micro):
    summ = 0.0
    for i in range(1, num_micro):
        summ += 1/(m.sin(i*m.pi/(float(num_micro))))
      #  print summ, '    ', num_micro

    return summ


summ = 0
num_micro = 1
micro_array = []
x_array = []

for charge in range(2, 1000):          #changing charge of macroion
    x_array.append(charge)
    while summ < charge:
        summ = 0.0
        summ = sinc(num_micro)
        num_micro += 1



    micro_array.append((num_micro-1)/float(charge))
    



pl.plot(x_array, micro_array)
pl.show()
