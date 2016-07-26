import matplotlib.pyplot as plt
import math as m
import numpy as np

def read(error, potential):

    with open('x_vals_for_error_'+str(error)+'_potential_' + str(potential) + '.txt', 'r') as f:
        results = f.readlines()

    return results



def find_L(potential):

    with open('inter_plate_dist_'+ str(potential)+'.txt', 'r') as f:                    #Function that reads the values of L from a text file.
        pop = f.readlines()



    return pop


error = 0.9
fig = plt.figure()
ax = fig.gca()



for potential in [2.35, 4.35]:
    L = find_L(potential)
    results2 = read(error, potential)

    results3 = [float(results2[i]) for i in range(len(results2))]
    
    if potential == 4.35:
        plt.plot(L, results3, label = 'Surface potential = ' + str(potential) + ' KbT', linestyle='-.')
    else:

    
        plt.plot(L, results3, label = 'Surface potential = ' + str(potential) + ' KbT')

    

plt.xlabel('Inter-plate Separation [Debye Lengths]', fontsize='16')
plt.ylabel('Width [Inter-Plate separation]', fontsize='16')
plt.title('Width of the Dressed Macroion in terms of Inter-Plate Separation for ' + str((1-error)*100) + '% error', fontsize='16')
plt.legend(loc=0, fontsize='16')
plt.grid()
plt.show()


