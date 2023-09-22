from __future__ import print_function
import matplotlib as mpl
#from matplotlib import pyplot;
from matplotlib.ticker import AutoMinorLocator
#mpl.use('Agg')
mpl.rcParams["axes.labelsize"]=40
mpl.rcParams["xtick.labelsize"]=40
mpl.rcParams["ytick.labelsize"]=40
mpl.rcParams["legend.fontsize"]=40
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


temps = [1,2,3,4,5,6,7,8,9,10,11,12]
names = ["hes","ndo","nbo","cao"]
labels = ["HES","NDO","NBO","CAO"]

def movingaverage (values, window):
    weights = np.ones([window,1])/window
    sma = convolve(values, weights, 'valid')
    print(sma.shape)
    return sma
J=0
remove = [12218,14635,14703,14618]
for I in names:
  n = genfromtxt("{}.dat".format(I))
  n1=movingaverage(n,50)
  nats.append(n)
  n1ats.append(n1)
  vnats.append(n[:,1])

fig,((ax1,ax2))= plt.subplots(1, 2, sharey='row',figsize=(20,10),width_ratios=[2, 1.5])
colors = ['blue',  'maroon', 'fuchsia', 'aqua']
for I in range(len(nats)):
  ax1.plot(nats[I][:,0],nats[I][:,1],color=colors[I],lw=2.0,markersize=0,alpha=0.2)
#  ax1.plot(n1ats[I][:,0],n1ats[I][:,1],label="{}".format(labels[I]),color=colors[I],lw=2.0,markersize=0)
  ax1.plot(n1ats[I][:,0],n1ats[I][:,1],color=colors[I],lw=2.0,markersize=0)

sb.violinplot(ax=ax2,data=vnats, palette=('Blue',  'Maroon', 'Fuchsia', 'Aqua'),width=1.0)


labels = ["HES","NDO","NBO","CAO"]
ax1.set_ylim(ymax= 23,ymin=5)
ax1.set_xlim(xmin=0,xmax=610)
ax2.set_ylim(ymin=5,ymax=23)
ax2.set_xticklabels(labels,rotation = 45,fontsize=45)
#ax1.annotate("A", xy=(0,85),fontsize=30)
#ax3.annotate("B", xy=(0,23),fontsize=30)
#leg = ax1.legend(handlelength=0.8, fontsize=45,ncol=2,)
#for line in leg.get_lines():
#    line.set_linewidth(4)
#leg.get_frame().set_edgecolor('black')
for I in (ax1,ax2):
  I.grid(linestyle="-",linewidth = 2 )

ax1.set_ylabel("Distance $\mathrm{d_b}$($\mathrm{\AA}$)",fontsize=45)
ax1.xaxis.set_major_locator(plt.MultipleLocator(200))
ax1.yaxis.set_major_locator(plt.MultipleLocator(10))
ax1.set_xlabel("Simulation time (ns)",fontsize=45)
#ax4.set_xlabel("Probability density",fontsize=26)
#ax.fill_between([mats[0][1000,0]/10,mats[0][1999,0]/10],[27,27],[46,46],alpha=0.3,color='C5')
ax2.spines['right'].set_visible(False)
plt.tight_layout()

plt.subplots_adjust(wspace=0.1)
fig.savefig('distance.png', format='png', dpi=300)
