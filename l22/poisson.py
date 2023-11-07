import scipy.integrate as spi
import scipy.special as sp
import numpy as np
import math
import matplotlib.pyplot as plt
plt.rcParams["axes.labelsize"]=12
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["legend.fontsize"]=12

fig,ax=plt.subplots()
l=2.5
x=np.arange(10)
y=((np.exp(-l))*(l**(x)))/sp.factorial(x)
print (y)
fig,ax = plt.subplots()
plt.plot(x,y,color='red',marker='o',lw=1.0,markersize=5,mfc='white',markevery=1)
ax.xaxis.set_major_locator(plt.MultipleLocator(2)) 
a=30
b=70
ax.set_xlabel("X",fontsize=16) 
ax.set_ylabel("$Poisson-distribution$",fontsize=16)
ax.set_xlim(0,20)

ax.grid(linestyle="--")
plt.savefig('poisson.png')
