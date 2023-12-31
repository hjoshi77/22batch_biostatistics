from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,10,1)
y = np.sin(x)
cs = CubicSpline(x, y)
print (cs)
xs = np.arange(-0.5, 9.6, 0.1)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'o', label='data')
#ax.plot(xs, np.sin(xs), label='true')
ax.plot(xs, cs(xs), label="S")
#ax.plot(xs, cs(xs, 1), label="S'")
#ax.plot(xs, cs(xs, 2), label="S''")
#ax.plot(xs, cs(xs, 3), label="S'''")
#ax.set_xlim(-0.5, 9.5)
ax.legend(loc='lower left', ncol=2)
plt.savefig("sine.png")

