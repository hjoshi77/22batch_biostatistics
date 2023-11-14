import numpy as np
import matplotlib.pyplot as plt
xn = np.linspace(-2,2,100)
for i in range(2,5):
  yn = xn**i
  print (i) 
  plt.plot(xn,yn)
plt.grid()
#plt.xlim(-0.01, 0.01)
plt.ylim(-0.01, 0.01)
plt.savefig('polynominal.png')
