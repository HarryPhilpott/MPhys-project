import numpy as np
import math as m
import matplotlib.pyplot as plt

# -*- coding: utf-8 -*-



x_range = []
results = []

for i in range(1000):

    if i != 0:
        err = i/1000.0
        x_range.append(err)

        results.append(m.sqrt(1-err)*err**-1)

    



plt.plot(x_range, results)


plt.title('Charge of Dressed Macroion Vs Error in  the Force', fontsize = 16)
plt.xlabel('Error in the Force', fontsize = 16)
plt.ylabel('Charge [Renorm constant]', fontsize = 16)


plt.grid()


plt.show()

