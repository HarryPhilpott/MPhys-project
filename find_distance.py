from scipy import special
import math as m
import numpy as np
from sympy import mpmath as mp



def calc(d):
    q = 1000.0
    N = 2356.0

    dval = -4*d*(d-1)**(-2)
    
    E = np.real(mp.ellipe(dval))
    F = np.real(mp.ellipf(dval))

    Ei = np.imag(mp.ellipe(dval)) 
    Fi = np.imag(mp.ellipf(dval))
    
    d4r = d**4*(E+F)
    d3r = -4*d**2*E
    d2r = d**2*(9*E+F-3*q*m.pi/N)
    d1r = d*(3*q*m.pi/N - 10*E)
    d0r = 4*E -2*F
s
    d4i = d**4*(Ei+Fi)
    d3i = -4*d**2*Ei
    d2i = d**2*(9*Ei+Fi-3*q*m.pi/N)
    d1i = d*(3*q*m.pi/N - 10*E)
    d0i = 4*Ei -2*Fi

    return (d4r+d3r+d2r+d1r+d0r), (d4i+d3i+d2i+d1i+d0i)

d = 1.436
result = 0.5
counter = 1



while counter > 0.001:
    real, imag = calc(d)
    print real , imag, d
    d = d + 0.001
    
##    if result > 0:
##        d = d + counter
    


