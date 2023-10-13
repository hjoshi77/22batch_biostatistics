import scipy.integrate as spi
import numpy as np
import math

# Define the parameters of the normal distribution
mean = 0  # Mean of the normal distribution
std_dev = 1  # Standard deviation of the normal distribution

# Define the normal distribution function
def y(x):
        return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))
# Define the integration limits
#a = -np.inf  # Lower limit (negative infinity)
a=0
b=2
#b = np.inf   # Upper limit (positive infinity)
# Perform the numerical integration
result, _ = spi.quad(y, a, b)
print(f"Integral of the normal distribution: {result:.6f}") 


