import scipy.integrate as spi
import scipy.special as sp
import numpy as np
import math
import matplotlib.pyplot as plt
plt.rcParams["axes.labelsize"]=12
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["legend.fontsize"]=12

n=100
def y(x):
        return ((sp.factorial(n))/(sp.factorial(n-x)*sp.factorial(x))) * ((p)**(x)) * ((1-p)**(n-x))

x=np.arange(n+1)
p=0.5
y=((sp.factorial(n))/(sp.factorial(n-x)*sp.factorial(x))) * ((p)**(x)) * ((1-p)**(n-x))
print (y)
fig,ax = plt.subplots()
plt.plot(x,y)
a=0
b=100
#plt.fill_between(x,y,where=((x>=a) & (x <=b)), alpha=0.3,color= 'C3')
ax.set_xlabel("X",fontsize=12) 
ax.set_ylabel("$Binomial-distribution$",fontsize=12)
result, _ = spi.quad(y, a, b)
print(f"Integral of the distribution: {result:.6f}")
#ax.set_ylim(0,0.40)
ax.grid(linestyle="--")

plt.savefig('binomial.png')
