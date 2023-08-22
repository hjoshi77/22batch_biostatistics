import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
 
# Creating dataset
#np.random.seed(23685752)
#N_points = 10000
n_bins = 10
mat0=np.loadtxt("inside_hst.dat") 
l=len(mat0[:,0])
# Creating distribution
 
# Creating histogram
fig, ax = plt.subplots()
ax.hist(mat0[:,1],bins=n_bins,density=False)
ax.set_xlabel("Angle ($^{\circ}$)",fontsize=16,fontweight='bold')
ax.set_ylabel("Probability",fontsize=16,fontweight='bold')

#ax.set_ylim(ymax= 2000,ymin=-50)
ax.set_xlim(xmax= 180,xmin=0)
plt.savefig('hst_raw.png', format='png',bbox_inches='tight',dpi=300)
