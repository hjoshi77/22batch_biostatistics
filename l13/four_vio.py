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


mats = []
nats = []
vmats = []
vnats = []
m1ats = []
n1ats = []


names = ["hes","ndo","nbo","cao"]
labels = ["HES","NDO","NBO","CAO"]

def movingaverage (values, window):
    weights = np.ones([window,1])/window
    sma = convolve(values, weights, 'valid')
    print(sma.shape)
    return sma
for I in names:
  n = genfromtxt("{}.dat".format(I))
  vnats.append(n[:,1])
fig,ax1=plt.subplots()
colors = ['blue',  'maroon', 'fuchsia', 'aqua']
sb.violinplot(data=vnats, palette=('Blue',  'Maroon', 'Fuchsia', 'Aqua'),width=1.0)


labels = ["HES","NDO","NBO","CAO"]
#ax1.set_ylim(ymax= 23,ymin=5)
#ax1.set_xlim(xmin=0,xmax=610)
#grid(linestyle="-",linewidth = 2 )

ax1.set_ylabel("Distance $\mathrm{d_b}$($\mathrm{\AA}$)",fontsize=12)
ax1.set_xlabel("Simulation time (ns)",fontsize=12)
plt.tight_layout()

fig.savefig('four.png', format='png', dpi=300)
