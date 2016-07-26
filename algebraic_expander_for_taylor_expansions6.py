import math as m
import sympy as sy
from mpmath import *



K_sq = []
K_cube = []
K_5 = []
K_7 = []
K_9 = []
term2 = []
term3 = []
term4 = []
term5 = []
K = []
Sn = []


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


values = []
values.append(0.0)
values.append(-0.5)
values.append(0.0)
values.append(-1.0/6.0 )                                           #H = 1/(9!), I = 1228/(9!), J = 5478/(9!)
values.append(1.0/120.0)
values.append(14.0/120.0)
values.append(-1.0/float(m.factorial(7)))
values.append(135.0*-1.0/float(m.factorial(7)))
values.append(1.0/float(m.factorial(9)))
values.append(1228.0*1.0/float(m.factorial(9)))
values.append(5478.0*1.0/float(m.factorial(9)))



def write(string, kval):
        
    with open('coeffs_for_kval__'+str(k_val)+'__.txt', 'a') as f:
        f.write(string + '\n')
        f.close()
        


def str2num2(dummy):
    string = list(dummy)
    length = len(string)
    num = 1.0
    accept = list('kABCDEFGHIJ')
    

    for j in range(length):

        if string[j] in accept:
            pos = accept.index(string[j])
            if  string[j+3] == '-':
                num = num*values[pos]**(-1.0*find_power(string, j+4))
            else:
                num = num*values[pos]**(find_power(string, j+4))
                

    return num




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

    K_col_terms = [0]*11
    term2_col_terms = [0]*11
    term3_col_terms = [0]*11
    term4_col_terms = [0]*11
    term5_col_terms = [0]*11
    powers = [i for i in range(12)]
    
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
        print power
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

        
for j in range(1,10):
    k_val = 0.9 + j*0.01
    values[0] = k_val
    values[2] = ellipk(k_val)
    collect('x')


    for i in range(len(term2_col_terms)):
        print term5[i]
        readline()
        sum1 = term2_col_terms[i] + term3_col_terms[i] + K_col_terms[i] + term4_col_terms[i] + term5_col_terms[i]
        
        if sum1 != 0:
            write(str(sum1), k_val)

    write(str(k_val), k_val)



    
