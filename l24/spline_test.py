from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
mat=np.loadtxt("test.dat")
x = mat[:,0]
y = mat[:,1]
xs = np.arange(-2.4, 1.2, 0.1)

cs = CubicSpline(x, y)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'o', label='data')
ax.plot(xs, cs(xs), label="S")
plt.show()
plt.savefig("spline.png")
