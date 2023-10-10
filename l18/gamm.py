import scipy.integrate as spi
import numpy as np
import math

# Define the gamma function to be integrated
def gamma_function(x):
    return math.gamma(x)  # You can also use scipy.special.gamma(x)

# Define the integration limits
a = 0  # Lower limit
b = 5  # Upper limit

# Perform the numerical integration
result, _ = spi.quad(gamma_function, a, b)

print(f"Integral of gamma function from {a} to {b}: {result:.6f}")
