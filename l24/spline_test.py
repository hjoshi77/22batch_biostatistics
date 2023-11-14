from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
mat=np.loadtxt("xy.dat")
x = mat[:,0]
y = mat[:,1]
xs = np.arange(2,6,0.01)
#xs = np.arange(-2.4, 1.2, 0.1)

cs = CubicSpline(x, y)
print (cs)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'o', label='data')
ax.plot(xs, cs(xs), label="S")
plt.legend()
plt.savefig('spline.png')
