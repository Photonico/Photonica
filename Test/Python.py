""" Python Test """

#%% 
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

#%%
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

#%%
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
    """ doc """
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

#%%

#### Interatonic potential

import numpy as np

A = 1; B = 2
m = 2; n = 3
step = 0.01
r = np.array(np.arange(step,10,step))

# Repulsive potential
rep = A/(r**n)
# Attractive potential
atp = -B/(r**m)
# Resulting potential
pot = rep + atp

import matplotlib; import matplotlib.pyplot as plt

plt.figure(dpi=192); params = {"text.usetex":True, "font.family":"serif", "mathtext.fontset":"cm", "axes.titlesize": 16, "axes.labelsize":14, "figure.facecolor":"w"}
matplotlib.rcParams.update(params)
plt.ticklabel_format(style="sci", scilimits=(0,0)); plt.tick_params(direction="in",top=True,right=True,bottom=True,left=True)
plt.title("Interatomic potential"); plt.xlabel(r"Interatomic distance"); plt.ylabel(r"Interatomic potential")
plt.xlim(0, 8); plt.ylim(-4, 4); 
plt.plot(r, rep, label="Repulsive potential", color="#FA3C3C")
plt.plot(r, atp, label="Attractive potential", color="#0A8CFF")
plt.plot(r, pot, label="Resulting potential", color="#6E64FA")
plt.plot(r, r*0, color="gray", alpha=0.4); plt.legend(loc="best")

import numpy as np
e = 2.71828182845904523536
k = 1.380649e-23
v = np.array(np.arange(0,2,0.001))
a = np.matrix([1,2,4,8,16,32,64])
n = 1/(e**np.array(a.T*np.matrix(v-1))+1)

#%%
#### Fermi-Dirac statistics
import matplotlib; import matplotlib.pyplot as plt
plt.figure(dpi=192); params = {"text.usetex":True, "font.family":"serif", "mathtext.fontset":"cm", "axes.titlesize": 16, "axes.labelsize":14, "figure.facecolor":"w"};
matplotlib.rcParams.update(params)
plt.ticklabel_format(style="sci", scilimits=(0,0)); plt.tick_params(direction="in",top=True,right=True,bottom=True,left=True)
plt.suptitle("The Fermi-Dirac Distribution", fontsize=16); plt.title("Energy dependence", fontsize=12); plt.xlabel(r"$E/\mu$"); plt.ylabel(r"$\langle{n_i}\rangle$", rotation=0)
plt.plot(([1,1]),([0,1]), "--", color="#A0A0A0"); plt.annotate(r"$\mu\approx E_F$", xy=(1.00, 0.85), xytext=(1.20, 0.95), arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=-0.2"))
plt.plot(v,n[0,:],label="$k_BT=\mu /1$", color="#FA3C3C")
plt.plot(v,n[1,:],label="$k_BT=\mu /2$", color="#FA9C3D")
plt.plot(v,n[2,:],label="$k_BT=\mu /4$", color="#FADC14")
plt.plot(v,n[3,:],label="$k_BT=\mu /8$", color="#50F050")
plt.plot(v,n[4,:],label="$k_BT=\mu /16$", color="#0A8CFF")
plt.plot(v,n[5,:],label="$k_BT=\mu /64$", color="#6E64FA")
plt.legend(loc="best")

#%%
#### Kinetic theory of gases

import numpy as np
T = np.arange(0,1000,1)
k = 1.380649e-23
m = np.matrix([2,28,32])*1.67e-27
v = np.sqrt(3*k*T/m.T)

import matplotlib; import matplotlib.pyplot as plt
plt.figure(dpi=192); params = {"text.usetex":True, "font.family":"serif", "mathtext.fontset":"cm", "axes.titlesize": 16, "axes.labelsize":14, "figure.facecolor":"white"}
matplotlib.rcParams.update(params)
plt.ticklabel_format(style="sci", scilimits=(0,0)); plt.tick_params(direction="in",top=True,right=True,bottom=True,left=True)
plt.title("Kinetic Theory of Gases"); plt.xlabel(r"Temperature ($\rm{K}$)"); plt.ylabel(r"Melocule Velocity ($\rm{ms^{-1}}$)")
plt.plot(T,np.array(v[0,:].T),label=r"Hydrogen $\rm{H_2}$", color="#0A8CFF")
plt.plot(T,np.array(v[1,:].T),label=r"Nitrogen $\rm{N_2}$", color="#FA3C3C")
plt.plot(T,np.array(v[2,:].T),label=r"Oxygen $\rm{O_2}$", color="#50F050"); plt.legend(loc="best")

#%%
#### Einstein's calculation

import numpy as np
Interval = 0.01
reT = np.arange(Interval,2+Interval,Interval)
reV = np.power(reT,-1)
reC = reV**2*np.exp(reV)/np.square(np.exp(reV)-1)

import matplotlib; import matplotlib.pyplot as plt
plt.figure(dpi=192); params = {"text.usetex":True, "font.family":"serif", "mathtext.fontset":"cm", "axes.titlesize": 16, "axes.labelsize":14, "figure.facecolor":"w"};
matplotlib.rcParams.update(params)
plt.ticklabel_format(style="sci", scilimits=(0,0)); plt.tick_params(direction="in",top=True,right=True,bottom=True,left=True)
plt.title("Einstein heat capacity per atom in three dimenson"); plt.xlabel(r"$k_BT/(\hbar\omega)$"); plt.ylabel(r"$\frac{C}{3k_B}$",rotation=0)
plt.plot(reT,reC,color="#0A8CFF")
