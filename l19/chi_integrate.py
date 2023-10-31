import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

import math

# Define the parameters of the normal distribution
mean = 0  # Mean of the normal distribution
std_dev = 1  # Standard deviation of the normal distribution

# Define the chi square distribution function
def y(x):
        k=50
        return (((x)**((k/2)-1))*np.exp(x*-0.5))/((2**(k/2))*math.gamma(k/2))
# Define the integration limits
x=np.linspace(0.1,100,100)
n=y(x)
a = 0.  # Lower limit (negative infinity)
#a=
b=70
#b = np.inf   # Upper limit (positive infinity)
# Perform the numerical integration
plt.plot(x,n)
plt.savefig('chi.png')
plt.fill_between(x,n,where=((x>=a) & (x <=b)), alpha=0.3,color= 'C3')
result, _ = spi.quad(y, a, b)
print(f"Integral of the chi-square distribution: {result:.6f}") 


