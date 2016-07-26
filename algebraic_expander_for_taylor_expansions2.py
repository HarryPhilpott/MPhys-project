import numpy as np
import math as m
import scipy as sci
import matplotlib.pyplot as plt

global K_cube, K_sq, cube_col_terms, sq_col_terms , sq_coeff, cube_coeff, term2, term3, K, co, k_val

k_val = 0.2
co = []

term2 = []
term3 = []
K = []

K_cube = []
K_sq = []





def str2num2(dummy):
    string = list(dummy)
    length = len(string)
    num = 1.0
    term2_coeff = [0]*27
    term3_coeff = [0]*27
    K_coeff = [0]*27
    A = m.pi/2.0
    B = m.pi/8.0                                    #A = pi/2, B = pi/8, C = 9pi/128, D = 25pi/512, E = 1225pi/32768
    C = 9.0*m.pi/128.0
    D = 25.0*m.pi/512.0
    E = 1225.0*m.pi/32768.0
    F = -0.5
    G = -1.0/6.0
    H = 1.0/120.0
    I = 14.0/120.0


    for j in range(length):

        if k_val != 0 and string[j] == 'k':
            if  string[j+3] == '-':
                num = num*k_val**(-1.0*float(''.join(string[j+4:j+7])))
            else:
                num = num*k_val**(float(''.join(string[j+4:j+7])))
        
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
                

        if string[j] == 'G':
            if  string[j+3] == '-':
                num = num*G**(-1.0*float(''.join(string[j+4:j+7])))
            else:
                num = num*G**(float(''.join(string[j+4:j+7])))

        if string[j] == 'H':
            if  string[j+3] == '-':
                num = num*H**(-1.0*float(''.join(string[j+4:j+7])))
            else:
                num = num*H**(float(''.join(string[j+4:j+7])))

        if string[j] == 'I':
            if  string[j+3] == '-':
                num = num*I**(-1.0*float(''.join(string[j+4:j+7])))
            else:
                num = num*I**(float(''.join(string[j+4:j+7])))

    return num





def Sn_function():
    global co
    tot = 0.0
    x_range = []
    vals = []
    
    for x in range(-2000,2000):
        for i in range(27):
            if x != 0:
                tot += float(co[i]*(abs(x)/1000.0)**(-3.0 + i*0.5))
                #print float(co[i]*(abs(x)/1000.0)**(-3.0 + i*0.5)), '     ', (-3.0 + i*0.5), '     ', co[i]

        x_range.append(float(x/1000.0))
        vals.append(tot)
        tot = 0.0
        

    return np.array(vals), np.array(x_range)

def reorder(string,var):
    dummy = list(string)
    length = len(string)

    if var not in dummy:
        return string


    pos = dummy.index(var)
    
    if dummy[pos+3] == '-':
        power = list(str(-1.0*float(''.join(dummy[pos+4:pos+7]))))
    else:
        power = list('+' + str(float(''.join(dummy[pos+4:pos+7]))))
        

    for i in range(pos, length-7):
        dummy[i] = dummy[i+7]

    dummy[length-7] = var
    dummy[length-6] = '^'
    dummy[length-5] = '('
    dummy[length-4:length-1] = power
    dummy[length] = ')'



    for i in range(length-1):
        if dummy[i] == ')' and dummy[i+1] == ')':
            dummy = dummy[:i] + dummy[i+1:]


    return ''.join(dummy)

    

def collect(var):
    global  term2, term3, K, term2_col_terms, term3_col_terms, K_col_terms

    K_col_terms = [0]*27
    term2_col_terms = [0]*27
    term3_col_terms = [0]*27
    powers = [-3.0+i*0.5 for i in range(27)]
    
    for k in range(len(term2)):
        string = list(term2[k])
        length = len(string)
        
        if var not in string:
            continue
            

        if  string[length - 5] == '-':
            comp_power = -1.0*float(''.join(string[length-4:length-1]))               
            
        else:
            comp_power = float(''.join(string[length-4:length-1]))

            
        concat = ''.join(string[:length-8])
        term2_col_terms[powers.index(comp_power)] += str2num2(concat)
        
        




    for k in range(len(K)):
        string = list(K[k])
        length = len(string)
        
        if var not in string:
            continue
            

        if  string[length - 5] == '-':
            comp_power = -1.0*float(''.join(string[length-4:length-1]))               
            
        else:
            comp_power = float(''.join(string[length-4:length-1]))

            
        concat = ''.join(string[:length-8])
        K_col_terms[powers.index(comp_power)] += str2num2(concat)



    for k in range(len(term3)):
        string = list(term3[k])
        length = len(string)
        
        if var not in string:
            continue
            

        if  string[length - 5] == '-':
            comp_power = -1.0*float(''.join(string[length-4:length-1]))               
            
        else:
            comp_power = float(''.join(string[length-4:length-1]))
            

        concat = ''.join(string[:length-8])
        term3_col_terms[powers.index(comp_power)] += str2num2(concat)
        


    

                    
def str2num(k_val):
    global K_coeff, term3_coeff, term2_coeff, term3_col_terms, term2_col_terms, K_col_terms

    num = 1.0
    term2_coeff = [0]*27
    term3_coeff = [0]*27
    K_coeff = [0]*27
    A = m.pi/2.0
    B = m.pi/8.0                                    #A = pi/2, B = pi/8, C = 9pi/128, D = 25pi/512, E = 1225pi/32768
    C = 9.0*m.pi/128.0
    D = 25.0*m.pi/512.0
    E = 1225.0*m.pi/32768.0
    F = -0.5
    G = -1.0/6.0
    H = 1.0/120.0
    I = 14.0/120.0



    
    for k in range(3):
        for i in range(24):
            if k == 0:
                string = list(term3_col_terms[i])
                #print 'number of term3 coeffs = ', -3.0 +i*0.5, '    ', len(string)
            if k == 1:
                string = list(term2_col_terms[i])
            if k == 2:
                string = list(K_col_terms[i])
                
            length = len(string)

            for j in range(length):
                    

                if k_val != 0 and string[j] == 'k':
                    if  string[j+3] == '-':
                        num = num*k_val**(-1.0*float(''.join(string[j+4:j+7])))
                    else:
                        num = num*k_val**(float(''.join(string[j+4:j+7])))
                    

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
                        

                if string[j] == 'G':
                    if  string[j+3] == '-':
                        num = num*G**(-1.0*float(''.join(string[j+4:j+7])))
                    else:
                        num = num*G**(float(''.join(string[j+4:j+7])))

                if string[j] == 'H':
                    if  string[j+3] == '-':
                        num = num*H**(-1.0*float(''.join(string[j+4:j+7])))
                    else:
                        num = num*H**(float(''.join(string[j+4:j+7])))

                if string[j] == 'I':
                    if  string[j+3] == '-':
                        num = num*I**(-1.0*float(''.join(string[j+4:j+7])))
                    else:
                        num = num*I**(float(''.join(string[j+4:j+7])))
                    

                
    return num




                  

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

    return reorder(concat, 'x')         
                

K = []                           

K.append('A^(+1.0)k^(+0.0)x^(+0.0)')                                                  #A = pi/2, B = pi/8, C = 9pi/128, D = 25pi/512, E = 1225pi/32768  F = -0.5
K.append('B^(+1.0)k^(+1.0)x^(+0.0)')
K.append('C^(+1.0)k^(+2.0)x^(+0.0)')
K.append('D^(+1.0)k^(+3.0)x^(+0.0)')
K.append('E^(+1.0)k^(+4.0)x^(+0.0)')
K.append('F^(+1.0)k^(-0.5)x^(+1.0)')

K_5 = []

Sn = []
term2 = []
term3 = []

Sn.append('G^(+1.0)k^(+0.0)x^(+0.0)')
Sn.append('G^(+1.0)k^(+2.0)x^(+0.0)')           #G = -1/6, H = 1/120, I = 14/120, 
Sn.append('H^(+1.0)k^(+0.0)x^(+0.0)')
Sn.append('I^(+1.0)k^(+2.0)x^(+0.0)')
Sn.append('H^(+1.0)k^(+4.0)x^(+0.0)')
coefficients = []

test = []
          


for i in range(len(K)):
    for j in range(len(K)):
        K_sq.append(terms(K[i]+K[j]))

##for i in range(len(K_sq)):
##    print K_sq[i]
        
        
for i in range(len(K)):
    for j in range(len(K_sq)):
        K_cube.append(terms(K_sq[j] + K[i]))
        

##for i in range(len(K)):
##    for j in range(len(K)):
##        for k in range(len(K)):
##            test.append(terms(K[i]+K[j]+K[k]))
##
##print len(test), len(K_cube)

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


collect('x')
#str2num(0.1)




for i in range(len(term2_col_terms)):
    co.append(term2_col_terms[i] + term3_col_terms[i] + K_col_terms[i])    #the final coefficients

for i in range(len(co)):
    if co[i] != 0:
        print co[i], -3.0+ i*0.5, co[i]/co[8]

fig = plt.figure()


ax = fig.add_subplot(1,1,1)

vals, x_range = Sn_function()

line1, = ax.plot(x_range, vals)
#line2, = ax.plot(x_range, lin_vals, label='Non-Linear Potential')
#line3, = ax.plot(x_range, abs_range, label='Actual Surface Potential')



ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
#ax.spines['bottom']#.set_position('center')
ax.spines['top'].set_color('black')
ax.spines['left'].set_smart_bounds(False)
ax.spines['bottom'].set_color('none')
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')
ax.grid()
#plt.xlim(0,1)
#plt.ylim(-3.5,0)
##plt.gca().set_aspect('equal', adjustable='box')
##ax.legend(loc=3)

#ax.axes.get_xaxis().set_ticks([0,0.1,0.2,0.3]) #,0.4,0.5,0.6,0.7,0.8,0.9,1.0])



plt.show()




    
