import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt 
d1=genfromtxt('india.dat',delimiter=',')
fig,ax=plt.subplots()
ax1=ax.twinx()
ax.plot(d1[:,6])
ax1.plot(d1[:,4],color='r')
ax.set_xlim(xmax=1300,xmin=0)
#ax.set_ylim=(y_max=1300,x_min=0)

ax.set_xlabel("Time since Covid (Days)",fontsize=16)
ax.set_ylabel("Cases",fontsize=16)
plt.tight_layout()
fig.savefig("new_cases.png",format='png',dpi=300,bbox_inches='tight')
