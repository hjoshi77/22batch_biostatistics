import scipy.integrate as spi
import numpy as np
import math
import matplotlib.pyplot as plt


# Define the parameters of the normal distribution
mean = 0  # Mean of the normal distribution
std_dev = 1  # Standard deviation of the normal distribution

# Define the normal distribution function
def y(x):
        return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))
# Define the integration limits
#a = -np.inf  # Lower limit (negative infinity)
fig,ax=plt.subplots()
a=-1
b=1
x=np.linspace(-5,5,100)
n=y(x) 
plt.plot(x,n)
#b = np.inf   # Upper limit (positive infinity)
# Perform the numerical integration
plt.fill_between(x,n,where=((x>=a) & (x <=b)), alpha=0.3,color= 'C3')
plt.fill_between(x,n,where=((x<=a) | (x >=b)), alpha=0.3,color= 'C1')

result, _ = spi.quad(y, a, b)
print(f"Integral of the normal distribution: {result:.6f}") 
ax.grid(linestyle="--")

plt.savefig('normal.png')

