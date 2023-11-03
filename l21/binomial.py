import scipy.integrate as spi
import scipy.special as sp
import numpy as np
import math
import matplotlib.pyplot as plt
plt.rcParams["axes.labelsize"]=12
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["legend.fontsize"]=12

def factorial(n):
# single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1)    
n=50
x=np.arange(n+1)
p=0.6
y=((sp.factorial(n))/(sp.factorial(n-x)*sp.factorial(x))) * ((p)**(x)) * ((1-p)**(n-x))
print (y)
fig,ax = plt.subplots()
plt.plot(x,y)
a=30
b=70
#plt.fill_between(x,y,where=((x>=a) & (x <=b)), alpha=0.3,color= 'C3')
ax.set_xlabel("X",fontsize=12) 
ax.set_ylabel("$Binomial-distribution$",fontsize=12)

#ax.set_ylim(0,0.40)
ax.grid(linestyle="--")

plt.savefig('binomial_50.png')
