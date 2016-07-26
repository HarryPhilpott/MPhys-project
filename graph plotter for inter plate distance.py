import matplotlib.pyplot as plt
import math as m



with open('inter_plate_dist_2.35.txt', 'r') as f:
    results = f.readlines()

with open('inter_plate_dist_4.35.txt', 'r') as f:
    results2 = f.readlines()

distance = [2.0*float(i) for i in results]
distance2 = [2.0*float(i) - 1.2 for i in results2]
x = [m.log(i/1000.0) for i in range(100, 1000)]
stop = False
i = 0

#while stop == False


plt.plot(distance, x, label = 'Surface potential = -2.35 KbT', linestyle='-.')
plt.plot(distance2, x, label = 'Surface potential = -4.35 KbT')
plt.title('Inter-Plate separation Vs. Mid-Plane potential', fontsize=16)
plt.ylabel('Mid-plane potential [KbT]', fontsize=16)
plt.xlabel('Inter-plate separation [Debye Lengths]', fontsize=16)
plt.grid()
plt.legend(loc=0, fontsize=16)

plt.show()
