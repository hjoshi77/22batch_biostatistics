import numpy as np
import matplotlib.pyplot as plt
x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
z = np.polyfit(x, y, 1)
f = np.poly1d(z)
plt.plot (x,y,marker='o',lw=0.0,markersize=10,mfc='white')
xn = np.linspace(0,5,100)
yn = f(xn)
plt.plot(xn,yn)
print(z)
plt.savefig('t.png')
