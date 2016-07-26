import math as m



def write(string, kval):
        
    with open('coeffs_for_kval__'+str(k_val)+'__.txt', 'a') as f:
        f.write(string + '\n')
        f.close()
        




def coeff_1(k):
    return -1.0*(1+k**2)/m.factorial(3.0)

def coeff_2(k):
    return (1.0+14.0*k**2.0+k**4.0)/m.factorial(5.0)

def coeff_3(k):
    return -1.0*(1+135.0*k**2 + 135.0*k**4 + k**6)/m.factorial(7.0)

def coeff_4(k):
    return (1.0 + 1228.0*k**2 + 5478.0*k**4 + 1228.0*k**6 + k**8)/m.factorial(9.0)

def coeff_5(k):
    return -1.0*(1.0 + 11069.0*k**2 + 165826.0*k**4 + 165826.0*k**6 + 11069.0*k**8 + k**10)/m.factorial(11.0)

def coeff_6(k):
    return  (1.0 + 99642.0*k**2 + 4494351.0*k**4 + 13180268.0*k**6 + 4494351.0*k**8 + 99642.0*k**10+ k**12)/m.factorial(13.0)

def coeff_7(k):
    return -1.0*(1.0 + 896803.0*k**2 + 116294673.0*k**4 + 834687179.0*k**6 + 834687179.0*k**8 + 116294673.0*k**10 + 896803*k**12 + k**14)/m.factorial(15.0)
    
def coeff_8(k):
    return  (1.0 + 8071256.0*k**2 + 2949965020.0*k**4 + 47152124264.0*k**6 + 109645021894.0*k**8 + 47152124264.0*k**10 + 2949965020.0*k**12 + 8071256*k**14 + k**16)/m.factorial(17.0)


        
for j in range(1,10):
    k_val = j*0.1


    write(str(1), k_val)
    write(str(coeff_1(k_val)), k_val)
    write(str(coeff_2(k_val)), k_val)
    write(str(coeff_3(k_val)), k_val)
    write(str(coeff_4(k_val)), k_val)
    write(str(coeff_5(k_val)), k_val)
    write(str(coeff_6(k_val)), k_val)
    write(str(coeff_7(k_val)), k_val)
    write(str(coeff_8(k_val)), k_val)
    write(str(k_val), k_val)
        
