import numpy as np
import math as m
import scipy as sci
import random as r

global K_cube, K_sq, cube_col_terms, sq_col_terms , sq_coeff, cube_coeff, term2, term3, K

term2, term3, K = []

K_cube = []
K_sq = []

sq_coeff = []
cube_coeff = []

def reorder(string):
    dummy = list(string)
    length = len(string)

    if 'k' not in dummy:
        return string


    pos = dummy.index('k')
    
    if dummy[pos+3] == '-':
        power = list(str(-1.0*float(''.join(dummy[pos+4:pos+7]))))
    else:
        power = list('+' + str(float(''.join(dummy[pos+4:pos+7]))))
        

    for i in range(pos, length-7):
        dummy[i] = dummy[i+7]

    dummy[length-7] = 'k'
    dummy[length-6] = '^'
    dummy[length-5] = '('
    dummy[length-4:length-1] = power
    dummy[length] = ')'



    for i in range(length-1):
        if dummy[i] == ')' and dummy[i+1] == ')':
            dummy = dummy[:i] + dummy[i+1:]


    return ''.join(dummy)

    

def collect():
    global  K_cube, K_sq, cube_col_terms, sq_col_terms 

    sq_col_terms = ['']*24
    cube_col_terms = ['']*24
    powers = [-1.5+i*0.5 for i in range(24)]
    
    for k in range(len(K_sq)):
        string = list(K_sq[k])
        length = len(string)
        
        if 'k' not in string:
            continue
            

        if  string[length - 5] == '-':
            comp_power = -1.0*float(''.join(string[length-4:length-1]))               
            
        else:
            comp_power = float(''.join(string[length-4:length-1]))    
        
        sq_col_terms[powers.index(comp_power)] += ''.join(string[:length-8]) + ' + '




    for k in range(len(K_cube)):
        string = list(K_cube[k])
        length = len(string)
        
        if 'k' not in string:
            continue
            

        if  string[length - 5] == '-':
            comp_power = -1.0*float(''.join(string[length-4:length-1]))               
            
        else:
            comp_power = float(''.join(string[length-4:length-1]))    
        
        cube_col_terms[powers.index(comp_power)] += ''.join(string[:length-8]) + ' + '



                    
def str2num():
    global sq_coeff, cube_coeff

    num = 1.0
    cube_coeff = [0]*24
    sq_coeff = [0]*24
    A = m.pi/2.0
    B = m.pi/8.0                                    #A = pi/2, B = pi/8, C = 9pi/128, D = 25pi/512, E = 1225pi/32768
    C = 9.0*m.pi/128.0
    D = 25.0*m.pi/512.0
    E = 1225.0*m.pi/32768.0
    F = -0.5

    for i in range(24):
        string = list(cube_col_terms[i])
        length = len(string)

        for j in range(length):

            if string[j] == 'A':

                if  string[j+3] == '-':
                    num = num*A**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*A**(float(''.join(string[j+4:j+7])))
                

            if string[j] == 'B':
                if  string[j+3] == '-':
                    num = num*B**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*B**(float(''.join(string[j+4:j+7])))
                    

            if string[j] == 'C':
                if  string[j+3] == '-':
                    num = num*C**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*C**(float(''.join(string[j+4:j+7])))
                

            if string[j] == 'D':
                if  string[j+3] == '-':
                    num = num*D**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*D**(float(''.join(string[j+4:j+7])))
                

            if string[j] == 'E':
                if  string[j+3] == '-':
                    num = num*E**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*E**(float(''.join(string[j+4:j+7])))

            if string[j] == 'F':
                if  string[j+3] == '-':
                    num = num*F**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*F**(float(''.join(string[j+4:j+7])))
                

            if string[j] == '+':
                cube_coeff[i] += num
                num = 1.0

    num = 1.0


    for i in range(24):
        string = list(sq_col_terms[i])
        length = len(string)

        for j in range(length):
            if string[j] == 'A':

                if  string[j+3] == '-':
                    num = num*A**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*A**(float(''.join(string[j+4:j+7])))
                

            if string[j] == 'B':
                if  string[j+3] == '-':
                    num = num*B**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*B**(float(''.join(string[j+4:j+7])))
                    

            if string[j] == 'C':
                if  string[j+3] == '-':
                    num = num*C**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*C**(float(''.join(string[j+4:j+7])))
                

            if string[j] == 'D':
                if  string[j+3] == '-':
                    num = num*D**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*D**(float(''.join(string[j+4:j+7])))
                

            if string[j] == 'E':
                if  string[j+3] == '-':
                    num = num*E**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*E**(float(''.join(string[j+4:j+7])))

            if string[j] == 'F':
                if  string[j+3] == '-':
                    num = num*F**(-1.0*float(''.join(string[j+4:j+7])))
                else:
                    num = num*F**(float(''.join(string[j+4:j+7])))

            if string[j] == '+':
                sq_coeff[i] += num
                num = 1.0



                  

def terms(string):
    concat = ''
    checked_char = []
    exclude = ['0', '^', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '-', '&', '.','+']
    characters = list(string)
    length = len(characters)
    i = 0
    char_counter = 0
    
    for i in range(length):
        
        if characters[i] not in exclude:
            
            if characters[i+3] == '-':
                char_counter += -1.0*float(''.join(characters[i+4:i+7]))
            else:
                char_counter += float(''.join(characters[i+4:i+7]))
        


    
        for j in range(i+1, length):
            if characters[j] == characters[i] and characters[j] not in exclude:
                
                if characters[j+3] == '-':
                    char_counter += -1.0*float(''.join(characters[j+4:j+7]))
                else:
                    char_counter += float(''.join(characters[j+4:j+7]))
                    

                    
                characters[j] = '&'


        if char_counter > 9:
            return '0'
           
        

        if characters[i] not in exclude:
            if char_counter >= 0:
                concat += str(characters[i]) + '^(+' + str(char_counter) + ')'
            else:
                concat += str(characters[i]) + '^(' + str(char_counter) + ')'


        i += 1
        char_counter = 0  

    return reorder(concat)         
                

K = []                           

K.append('A^(+1.0)k^(+0.0)')                                                  #A = pi/2, B = pi/8, C = 9pi/128, D = 25pi/512, E = 1225pi/32768  
K.append('B^(+1.0)k^(+1.0)')
K.append('C^(+1.0)k^(+2.0)')
K.append('D^(+1.0)k^(+3.0)')
K.append('E^(+1.0)k^(+4.0)')
K.append('F^(+1.0)k^(-0.5)')

K_5 = []

Sn = []
term2 = []
term3 = []

Sn.append('G^(+1.0)')
Sn.append('G^(+1.0)k^(+2.0)')           #G = -1/6, H = 1/120, I = 14/120, 
Sn.append('H^(+1.0)')
Sn.append('I^(+1.0)k^(+2.0)')
Sn.append('H^(+1.0)k^(+4.0)')
          


for i in range(len(K)):
    for j in range(len(K)):
        K_sq.append(terms(K[i]+K[j]))
        
        
for i in range(len(K)):
    for j in range(len(K_sq)):
        K_cube.append(terms(K_sq[j] + K[i]))
        

for i in range(len(K_cube)):
    for j in range(len(K_sq)):
        K_5.append(terms(K_sq[j]+K_cube[i]))
        

for i in range(2):
    for j in range(len(K_cube)):
        term2.append(terms(Sn[i] + K_cube[j]))
        

for i in range(2,5):
    for j in range(len(K_5)):
        term3.append(terms(Sn[i] + K_5[j]))
        
final_terms = term3 + term2 + K


collect()
str2num()



for i in range(len(cube_coeff)):
    print sq_coeff[i], '     ', cube_coeff[i], '     ', -1.5+i*0.5

