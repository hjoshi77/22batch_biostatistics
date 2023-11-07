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
n1 = range(101)
for n in n1:  
  x=np.arange(n+1)
  p=0.5
  n=float(n)
  y=((sp.factorial(n))/(sp.factorial(n-x)*sp.factorial(x))) * ((p)**(x)) * ((1-p)**(n-x))
##print (y)
  fig,ax = plt.subplots()
  plt.plot(x,y)
  ax.set_xlabel("X",fontsize=12) 
  ax.set_ylabel("$Binomial-distribution$",fontsize=12)

  ax.set_xlim(0,100)
  ax.grid(linestyle="--")

  plt.savefig('binomial{}.png'.format(n))
