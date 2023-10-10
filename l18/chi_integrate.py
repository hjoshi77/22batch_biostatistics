import scipy.integrate as spi
import numpy as np
import math

# Define the parameters of the normal distribution
mean = 0  # Mean of the normal distribution
std_dev = 1  # Standard deviation of the normal distribution

# Define the normal distribution function
def y(x):
        k=3
        return (((x)**((k/2)-1))*np.exp(x*-0.5))/((2**(k/2))*math.gamma(k/2))
# Define the integration limits
a = 0  # Lower limit (negative infinity)
#a=
b=0.5
#b = np.inf   # Upper limit (positive infinity)
# Perform the numerical integration
result, _ = spi.quad(y, a, b)
print(f"Integral of the chi-square distribution: {result:.6f}") 


