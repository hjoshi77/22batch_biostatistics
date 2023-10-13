import scipy.integrate as spi
import numpy as np
import math
import matplotlib.pyplot as plt
plt.rcParams["axes.labelsize"]=12
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["legend.fontsize"]=12

# Define the parameters of the normal distribution
mean = 0  # Mean of the normal distribution
std_dev = 1  # Standard deviation of the normal distribution

# Define the normal distribution function
def gamma_function(x):
        return math.gamma(x)  # You can also use scipy.special.gamma(x)

## Define T-Distribution PDF 
def y(x):
        n=1
        return (gamma_function((n+1)/2))/((np.sqrt((np.pi)*n)) * (gamma_function(n/2)) * ((1 +x**2)**((n+1)/2))/n)

# Define the integration limits
#a = -np.inf  # Lower limit (negative infinity)
a=-12.71
b=12.71
#b = np.inf   # Upper limit (positive infinity)
# Perform the numerical integration
x=np.linspace(-20,20,100)
n=y(x)
fig,ax = plt.subplots()
plt.plot(x,n)
plt.fill_between(x,n,where=((x>=a) & (x <=b)), alpha=0.3,color= 'C3')
ax.set_xlabel("X",fontsize=12) 
ax.set_ylabel("$T-distribution$",fontsize=12)

ax.set_ylim(0,0.40)
ax.grid(linestyle="--")

plt.savefig('t.png')
result, _ = spi.quad(y, a, b)
print(f"Integral of the T distribution: {result:.6f}") 


