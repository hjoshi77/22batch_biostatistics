from __future__ import print_function
import matplotlib as mpl
#from matplotlib import pyplot;

import math
from matplotlib.ticker import AutoMinorLocator
#mpl.use('Agg'
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

mat0 = genfromtxt("watnum.dat");
#mat1 = genfromtxt("/data/server2/hjoshi/projects/f25/mem/keep_water_away/analysis/watnum.dat");
#mat2 = genfromtxt("/data/server7/hjoshi/projects/hp-la1/c1/analysis/test/watnum.dat");
#mat3 = genfromtxt("/data/server7/hjoshi/projects/hp-la1/2C_17/analysis/watnum.dat");
#mat3 = genfromtxt("/data/server7/hjoshi/projects/peptide_channels/karl/aqua/run/analysis/watnum.dat");
def movingaverage (values, window):
    #weights = np.repeat(1.0, window)/window
    weights = np.ones([window,1])/window
    sma = convolve(values, weights, 'valid')
    print(sma.shape)
    return sma
fig,ax = plt.subplots()
ax.plot(mat0[::20,0], mat0[::20,1], color='magenta',marker='o',lw=1.0,markersize=7,mfc='white',markevery=2,label="F25 (run 1)")
#ax.plot(mat3[:,0], mat3[:,1], color='red',marker='^',lw=1.0,markersize=0,mfc='white',markevery=40,label='C2-17 (run 2)');
#legend = plt.legend(frameon="1")
#plt.grid(linestyle=":")
#plt.grid(color='r', linestyle='.', linewidth=0.2)
plt.legend(handlelength=0,loc=0,frameon="True",fontsize=10)
#plt.legend(handlelength=0,loc=0,frameon="True",fontsize=12,bbox_to_anchor=(0.3,0.6))
plt.minorticks_off()
ax.tick_params(direction='in')
#ax.xaxis.set_minor_locator(plt.MultipleLocator(200))
#ax.yaxis.set_minor_locator(plt.MultipleLocator(250))
ax.set_xlabel("Simulation time (ns)",fontsize=12)
ax.set_ylabel("Permeated water molecules",fontsize=12) 

#ax.set_ylim(ymax= 2000,ymin=-50)
#ax.set_xlim(xmax= 200,xmin=0)
#x.yaxis.set_minor_locator(plt.MultipleLocator(.1))
#ax.fill_between([20,35],[-3,-3],[18,18],alpha=0.1,color='C4')
#ax.fill_between([50,80],[0,0],[5000,5000],alpha=0.3,color='C1')
#ax.fill_between([0,50],[0,0],[5000,5000],alpha=0.3,color='C0')

plt.tight_layout()
#plt.show()
#fig.savefig('water_per.pdf', format='pdf',bbox_inches='tight',dpi=300)
fig.savefig('watnum.png', format='png',bbox_inches='tight',dpi=300)
