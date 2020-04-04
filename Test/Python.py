#### Lagrange Interpolation Formula

import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

to = time.time()

def lagrange_interpolate(x, y, t):
    p = lagrange(x, y)
    return p(t)

x, y = np.loadtxt('Data/dataSim.dat', unpack=True)
t = np.linspace(1, 2, 11)
u = lagrange_interpolate(x, y, t)

td = time.time() - to
print("The time interval is %f s." %td)

plt.rcParams['font.family'] = 'CMU Serif'
plt.plot(t, u, "P", c="#00B4DC", alpha=0.9)
plt.plot(x, y, "o", c="#32B432", alpha=0.9)
plt.tick_params(direction='in')
plt.show()

#### Shanks Transform

import numpy as np
import matplotlib.pyplot as plt

"""
L[i] = (S[i]^2-S[i-1]*S[i+1])/(2*S[i]-S[i-1]-S[i+1])
"""

# Load Harmonic Series
X,Y = np.loadtxt('Data/Tr.dat', unpack=True)

count = len(X)

## L1
L1 = np.empty(count)
for i in range(0,count):
    if i > 0 and i < count-1:
        L1[i] = (Y[i]**2-Y[i-1]*Y[i+1])/(2*Y[i]-Y[i-1]-Y[i+1])
    else:
        L1[i] = 0
    i = i + 1

## L2
L2 = np.empty(count)
for i in range(0,count):
    if i > 0 and i < count-1:
        L2[i] = (L1[i]**2-L1[i-1]*L1[i+1])/(2*L1[i]-L1[i-1]-L1[i+1])
    else:
        L2[i] = 0
    i = i + 1

## L3
L3 = np.empty(count)
for i in range(0,count):
    if i > 0 and i < count - 1:
        L3[i] = (L2[i]**2-L2[i-1]*L2[i+1])/(2*L2[i]-L2[i-1]-L2[i+1])
    else:
        L3[i] = 0
    i = i + 1

## L4
L4 = np.empty(count)
for i in range(0,count):
    if i > 0 and i < count - 1:
        L4[i] = (L3[i]**2-L3[i-1]*L3[i+1])/(2*L3[i]-L3[i-1]-L3[i+1])
    else:
        L4[i] = 0     
    i = i + 1

plt.rcParams['font.family'] = 'CMU Serif'
plt.plot(X, Y, "o", c="#B4B4B4", alpha=0.9)
plt.plot(X[1:len(L1)-1], L1[1:len(L1)-1], c="#FF1E14", alpha=0.9)
plt.plot(X[2:len(L1)-2], L2[2:len(L1)-2], c="#FFC814", alpha=0.9)
plt.plot(X[3:len(L1)-3], L3[3:len(L1)-3], c="#1978F0", alpha=0.9)
plt.plot(X[4:len(L1)-4], L4[4:len(L1)-4], c="#A064DC", alpha=0.9)

plt.tick_params(direction='in')
plt.show()

#### Richardson Extrapolation

import numpy as np
import time
import matplotlib.pyplot as plt

"""
Sn = 1 + 1/2^2 + 1/3^2 + 1/4^2 + ... + 1/n^2
lim(n->∞)Sn = π^2/6 ≈ 1.6449340668482264

R1(n) = ((n+1)*S(n+1)-n*S(n))/np.math.factorial(1)
R2(n) = ((n+2)^2*S(n+1)-2*(n+1)^2*S(n+1)+n^2*S(n))/np.math.factorial(2)
……
"""

to = time.time()

X,Y = np.loadtxt('Data/Td.dat', unpack=True)

count = len(X)

def RE1(Y):
    R1 = np.ones(count)
    for i in range(0, count - 1):
        if i < count - 1 :
            R1[i] = ((i+1)*Y[i+1]-i*Y[i])/np.math.factorial(1)
        else:
            R1[i] = 0
        i = i + 1
    return R1

def RE2(Y):
    R2 = np.ones(count)
    for i in range(0, count - 2):
        if i < count - 2 :
            R2[i] = ((i+2)**2*Y[i+2]-2*(i+1)**2*Y[i+1]+i**2*Y[i])/np.math.factorial(2)
        else:
            R2[i] = 0
        i = i + 1
    return R2

U1 = RE1(Y)
U2 = RE2(Y)

td = time.time() - to
print("The time interval is %f s." %td)

plt.rcParams['font.family'] = 'CMU Serif'
plt.plot(X, Y, "o", c="#B4B4B4", alpha=0.9)
plt.plot(X[0:len(U1)-1], U1[0:len(U1)-1], c="#FF1E14", alpha=0.9)
plt.plot(X[0:len(U1)-2], U2[0:len(U1)-2], c="#1978F0", alpha=0.9)
plt.tick_params(direction='in')
plt.show()