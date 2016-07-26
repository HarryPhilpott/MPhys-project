import numpy as np
import math as m
import scipy as sci
import matplotlib.pyplot as plt
import sympy as sy
from mpmath import *

global K_cube, K_sq, term2, term3, K, co, k_val, term4, term_5

k_val = 0.1
co = []
term2 = []
term3 = []
term4 = []
term5 = []
K = []
K_cube = []
K_sq = []
K_5 = []
K_7 = []
K_9 = []
Sn = []


def str2num2(dummy):
    string = list(dummy)
    length = len(string)
    num = 1.0
    pi = m.pi
    term2_coeff = [0]*60
    term3_coeff = [0]*60
    K_coeff = [0]*60
    A = -0.5
    B = ellipk(k_val)
    C = -1.0/6.0                                            #H = 1/(9!), I = 1228/(9!), J = 5478/(9!)
    D = 1.0/120.0
    E = 14.0/120.0
    F = -1.0/float(m.factorial(7))
    G = 135.0*F
    H = 1.0/float(m.factorial(9))
    I = 1228.0*H
    J = 5478.0*H




    for j in range(length):

        if string[j] == 'k':
            if  string[j+3] == '-':
                pass
                num = num*k_val**(-1.0*float(''.join(string[j+4:j+7])))
            else:
                num = num*k_val**(find_power(string, j+4))
        
        if string[j] == 'A':
            if  string[j+3] == '-':
                num = num*A**(-1.0*(find_power(string, j+4)))
            else:
                num = num*A**find_power(string, j+4)
                   

        if string[j] == 'B':
            if  string[j+3] == '-':
                num = num*B**(-1.0(*find_power(string, j+4)))
            else:
                num = num*B**(find_power(string, j+4))
                

        if string[j] == 'C':
            if  string[j+3] == '-':
                num = num*C**(-1.0*(find_power(string, j+4)))
            else:
                num = num*C**(find_power(string, j+4))
            

        if string[j] == 'D':
            if  string[j+3] == '-':
                num = num*D**(-1.0*(find_power(string, j+4)))
            else:
                num = num*D**(find_power(string, j+4))
            

        if string[j] == 'E':
            if  string[j+3] == '-':
                num = num*E**(-1.0*(find_power(string, j+4)))
            else:
                num = num*E**(find_power(string, j+4))


        if string[j] == 'F':
            if  string[j+3] == '-':
                num = num*F**(-1.0*(find_power(string, j+4)))
            else:
                num = num*F**(find_power(string, j+4))
                

        if string[j] == 'G':
            if  string[j+3] == '-':
                num = num*G**(-1.0*(find_power(string, j+4)))
            else:
                num = num*G**(find_power(string, j+4))

        if string[j] == 'H':
            if  string[j+3] == '-':
                num = num*H**(-1.0*(find_power(string, j+4)))
            else:
                num = num*H**(find_power(string, j+4))

        if string[j] == 'I':
            if  string[j+3] == '-':
                num = num*I**(-1.0*(find_power(string, j+4)))
            else:
                num = num*I**(find_power(string, j+4))

        if string[j] == 'J':
            if  string[j+3] == '-':
                num = num*J**(-1.0*(find_power(string, j+4)))
            else:
                num = num*J**(find_power(string, j+4))


    return num



def Sn_function():
    global co
    tot = 0.0
    x_range = []
    vals = []    
    
    for x in range(-1000,1000):
        for i in range(60):
            if x == 0:
                tot += float(co[i]*(abs(x-1)/1000.0)**(-15.0 + i*0.5))
            else:
                tot += float(co[i]*(abs(x)/1000.0)**(-15.0 + i*0.5))
                

        vals.append(2*m.log(abs(tot)))
        x_range.append(float(x/1000.0))
        tot = 0.0
            


    return np.array(vals), np.array(x_range)

def reorder(string,var):
    dummy = list(string)
    length = len(string)

    if var not in dummy:
        return string


    pos = dummy.index(var)
    
    if dummy[pos+3] == '-':
        power = list(str(-1.0*find_power(string, pos+4)))
    else:
        power = list('+' + str(find_power(string, pos+4)))
        

    for i in range(pos, length-7):
        dummy[i] = dummy[i+7]

    dummy[length-len(power) - 3] = var
    dummy[length-len(power) - 2] = '^'
    dummy[length-len(power) - 1] = '('
    dummy[length-len(power):length-1] = power
    dummy[length] = ')'



    for i in range(length-1):
        if dummy[i] == ')' and dummy[i+1] == ')':
            dummy = dummy[:i] + dummy[i+1:]


    return ''.join(dummy)

    

def collect(var):
    global  term2, term3, K, term2_col_terms, term3_col_terms, K_col_terms, term4_col_terms, term5_col_terms

    K_col_terms = [0]*60
    term2_col_terms = [0]*60
    term3_col_terms = [0]*60
    term4_col_terms = [0]*60
    term5_col_terms = [0]*60
    powers = [-15.0+i*0.5 for i in range(60)]
    
    for k in range(len(term2)):
        string = list(term2[k])
        length = len(string)
        
        if var not in string:
            continue
            

        if  string[length - 5] == '-':
            comp_power = -1.0*find_power(string, length - 4)              
            
        else:
            comp_power = find_power(string, length - 4)

            
        concat = ''.join(string[:length-8])
        term2_col_terms[powers.index(comp_power)] += str2num2(concat)
        


    for k in range(len(K)):
        string = list(K[k])
        length = len(string)
        
        if var not in string:
            continue
            

        if  string[length - 5] == '-':
            comp_power = -1.0*find_power(string, length - 4)              
            
        else:
            comp_power = find_power(string, length - 4)

            
        concat = ''.join(string[:length-8])
        K_col_terms[powers.index(comp_power)] += str2num2(concat)



    for k in range(len(term3)):
        string = list(term3[k])
        length = len(string)
        
        if var not in string:
            continue
            

        if  string[length - 5] == '-':
            comp_power = -1.0*find_power(string, length - 4)             
            
        else:
            comp_power = find_power(string, length - 4)
            

        concat = ''.join(string[:length-8])
        term3_col_terms[powers.index(comp_power)] += str2num2(concat)


    for k in range(len(term4)):
        string = list(term4[k])
        length = len(string)
        
        if var not in string:
            continue
            

        if  string[length - 5] == '-':
            comp_power = -1.0*find_power(string, length - 4)              
            
        else:
            comp_power = find_power(string, length - 4)
            

        concat = ''.join(string[:length-8])
        term4_col_terms[powers.index(comp_power)] += str2num2(concat)


    for k in range(len(term5)):
            string = list(term5[k])
            length = len(string)
            
            if var not in string:
                continue
                

            if  string[length - 5] == '-':
                comp_power = -1.0*find_power(string, length - 4)

                
            else:
                comp_power = find_power(string, length - 4)
                

            concat = ''.join(string[:length-8])
            term5_col_terms[powers.index(comp_power)] += str2num2(concat)


        
def find_power(string,i):
    characters = list(string)
    start = i
    power = ''
    exclude = list('ABCDEFGHIJKLxk')

    while characters[i] != ')':
        
        if characters[i] in exclude:
            return float(power)
        
        power += ''.join(characters[i])
        i += 1
        
    try:
        return float(power)
    except:
        print characters[start-5:i]
        return


                  

def terms(string):
    concat = ''
    exclude = ['0', '^', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '-', '&', '.','+']
    characters = list(string)
    length = len(characters)
    i = 0
    char_counter = 0
    
    for i in range(length):
        
        if characters[i] not in exclude:
            
            if characters[i+3] == '-':
                char_counter += -1.0*find_power(string, i+4)
            else:
                char_counter += find_power(string, i+4)
        


    
        for j in range(i+1, length):
            if characters[j] == characters[i] and characters[j] not in exclude:
                
                if characters[j+3] == '-':
                    char_counter += -1.0*find_power(string, j+4)
                else:
                    char_counter += find_power(string, j+4)
                    

                    
                characters[j] = '&'

           
        

        if characters[i] not in exclude:
            if char_counter >= 0:
                concat += str(characters[i]) + '^(+' + str(char_counter) + ')'
            else:
                concat += str(characters[i]) + '^(' + str(char_counter) + ')'


        i += 1
        char_counter = 0  

    return reorder(concat, 'x')         
                

                          


K.append('A^(+1.0)k^(-0.5)x^(+1.0)')
K.append('B^(+1.0)k^(+0.0)x^(+0.0)')                    #A = -0.5, B = K(k_val)



Sn.append('C^(+1.0)k^(+0.0)x^(+0.0)')
Sn.append('C^(+1.0)k^(+1.0)x^(+0.0)')           #C = -1/6, D = 1/120, E = 14/120, F = -1/(7!), G = -135/(7!) H = 1/(9!), I = 1228/(9!), J = 5478/(9!)

Sn.append('D^(+1.0)k^(+0.0)x^(+0.0)')
Sn.append('E^(+1.0)k^(+1.0)x^(+0.0)')
Sn.append('D^(+1.0)k^(+2.0)x^(+0.0)')

Sn.append('F^(+1.0)k^(+0.0)x^(+0.0)')
Sn.append('G^(+1.0)k^(+1.0)x^(+0.0)')
Sn.append('G^(+1.0)k^(+2.0)x^(+0.0)')
Sn.append('F^(+1.0)k^(+3.0)x^(+0.0)')

Sn.append('H^(+1.0)k^(+0.0)x^(+0.0)')
Sn.append('I^(+1.0)k^(+1.0)x^(+0.0)')
Sn.append('J^(+1.0)k^(+2.0)x^(+0.0)')
Sn.append('I^(+1.0)k^(+3.0)x^(+0.0)')
Sn.append('H^(+1.0)k^(+4.0)x^(+0.0)')

          


for i in range(len(K)):
    for j in range(len(K)):
        K_sq.append(terms(K[i]+K[j]))


        
for i in range(len(K)):
    for j in range(len(K_sq)):
        K_cube.append(terms(K_sq[j] + K[i]))
        


for i in range(len(K_cube)):
    for j in range(len(K_sq)):
        K_5.append(terms(K_sq[j]+K_cube[i]))

        

for i in range(len(K_sq)):
    for j in range(len(K_5)):
        K_7.append(terms(K_5[j]+K_sq[i]))

        
for i in range(len(K_7)):
    for j in range(len(K_sq)):
        K_9.append(terms(K_sq[j]+K_7[i]))


for i in range(2):
    for j in range(len(K_cube)):
        term2.append(terms(Sn[i] + K_cube[j]))
        

for i in range(2,5):
    for j in range(len(K_5)):
        term3.append(terms(Sn[i] + K_5[j]))
        

for i in range(5,9):
    for j in range(len(K_7)):
        term4.append(terms(Sn[i] + K_7[j]))

for i in range(9,14):
    for j in range(len(K_9)):
        term5.append(terms(Sn[i] + K_9[j]))

        

collect('x')


for i in range(len(term2_col_terms)):
    co.append(term2_col_terms[i] + term3_col_terms[i] + K_col_terms[i] + term4_col_terms[i] + term5_col_terms[i])    #the final coefficients

for i in range(len(co)):
    if co[i] != 0:
        print co[i], '   x^',-15.0+i*0.5

fig = plt.figure()


ax = fig.add_subplot(1,1,1)

vals, x_range = Sn_function()

line1, = ax.plot(x_range, vals)


##ax.spines['left'].set_position('center')
##ax.spines['right'].set_color('none')
###ax.spines['bottom']#.set_position('center')
##ax.spines['top'].set_color('black')
##ax.spines['left'].set_smart_bounds(False)
##ax.spines['bottom'].set_color('none')
##ax.xaxis.set_ticks_position('top')
##ax.yaxis.set_ticks_position('left')
##ax.grid()
#plt.xlim(-0.8,0.8)
#plt.ylim(-3.5,0)
##plt.gca().set_aspect('equal', adjustable='box')
##ax.legend(loc=3)

#ax.axes.get_xaxis().set_ticks([0,0.1,0.2,0.3]) #,0.4,0.5,0.6,0.7,0.8,0.9,1.0])



plt.show()




    
