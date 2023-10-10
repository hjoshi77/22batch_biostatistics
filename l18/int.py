import scipy.integrate as integrate
import numpy as np
import scipy.special as special
x = np.linspace(-1, 1, num=100)
std_dev=1
mean=0
y = x**2
y1= (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))
z=np.trapz(y, x)
z1=integrate.simpson(y1, x)
print (z,z1)
