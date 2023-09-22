from __future__ import print_function
import matplotlib as mpl
#from matplotlib import pyplot;
from matplotlib.ticker import AutoMinorLocator
#mpl.use('Agg')
mpl.rcParams["axes.labelsize"]=12
mpl.rcParams["xtick.labelsize"]=12
mpl.rcParams["ytick.labelsize"]=12
mpl.rcParams["legend.fontsize"]=12
mpl.rcParams['lines.linewidth'] = 2
from matplotlib import pyplot as plt
import numpy as np
import scipy.optimize as opt
from glob import glob
from pylab import genfromtxt
from scipy.signal import convolve
import scipy.optimize as opt
import seaborn as sb
from glob import glob



names = ["hes","ndo","nbo","cao"]
labels = ["HES","NDO","NBO","CAO"]

def movingaverage (values, window):
    weights = np.ones([window,1])/window
    sma = convolve(values, weights, 'valid')
    print(sma.shape)
    return sma
n = genfromtxt("hes.dat")
fig,ax1=plt.subplots()
colors = ['blue',  'maroon', 'fuchsia', 'aqua']
sb.violinplot(data=n[:,1], width=1.0)


labels = ["HES"]
ax1.set_ylim(ymax= 23,ymin=5)
#ax1.set_xlim(xmin=0,xmax=610)
ax1.grid(linestyle="-",linewidth = 2 )

ax1.set_ylabel("Distance $\mathrm{d_b}$($\mathrm{\AA}$)",fontsize=12)
plt.tight_layout()
ax1.set_xticklabels(labels,rotation = 0,fontsize=22)

fig.savefig('single.png', format='png', dpi=300)
