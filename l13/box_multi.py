import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import genfromtxt
mats = []

names = ["hes","ndo","nbo","cao"]
for I in names:
  n = np.genfromtxt("{}.dat".format(I))
  mats.append(n[:,1])

fig,ax=plt.subplots()
sns.boxplot(ax=ax,data=mats )
ax.grid(linestyle=":",linewidth = 0.2 )
ax.set_ylabel("Distance $\mathrm{d_b}$($\mathrm{\AA}$)",fontsize=15)

ax.set_xticklabels(names,rotation = 45,fontsize=15)

fig.savefig('box_multy.png', format='png', dpi=300)

