from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

import math


l=np.loadtxt("total_deaths.dat")

N=5
ind = np.arange(N)  # the x locations for the groups
width = 0.3    

fig, ax = plt.subplots()

c = ['C0', 'C1', 'C2', 'C3', 'C4']
ax.bar(ind, l, width, edgecolor = ["k"]*len(ind),capsize=3,color=c)
# for making hatch in structure
   
# done
ax.set_ylabel('Number of Lives lost',fontsize=16)
ax.set_xticks(ind )
plt.xticks(rotation=0)
ax.set_xticklabels(('USA','Brazil','India','Russia','Mexico'),fontsize=16)

plt.grid(linestyle=":")
plt.tight_layout()
fig.savefig('a2.png', format='png', dpi=300)
