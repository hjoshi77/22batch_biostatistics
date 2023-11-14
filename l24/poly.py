import numpy as np
import matplotlib.pyplot as plt
xn = np.linspace(-2,2,100)
for i in range(2,100):
  yn = (xn)**i+xn
  print (i) 
  plt.plot(xn,yn)
plt.grid()
plt.xlim(-1,1)
plt.ylim(-0.25, 0.25)
plt.savefig('polynominal.png')
