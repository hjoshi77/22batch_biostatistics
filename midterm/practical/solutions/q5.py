from __future__ import print_function
import matplotlib as mpl
#from matplotlib import pyplot;
from matplotlib.ticker import AutoMinorLocator
#mpl.use('Agg')
import pandas as pd
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
filepath = "./WHO-COVID-19-global-data.csv"
data = pd.read_csv(filepath)
vnats = []
usa = data[data['Country_code'] == 'US'][data.New_deaths > 100]['New_deaths']
braz = data[data['Country_code'] == 'BR'][data.New_deaths > 100]['New_deaths']
ind = data[data['Country_code'] == 'IN'][data.New_deaths > 100]['New_deaths']
rus = data[data['Country_code'] == 'RU'][data.New_deaths > 100]['New_deaths']
mex = data[data['Country_code'] == 'MX'][data.New_deaths > 100]['New_deaths']
vnats.append(usa)
vnats.append(braz)
vnats.append(ind)
vnats.append(rus)
vnats.append(mex)


labels = ["USA","Brazil","India","Russia","Mexico"]

def movingaverage (values, window):
    weights = np.ones([window,1])/window
    sma = convolve(values, weights, 'valid')
    print(sma.shape)
fig,ax1=plt.subplots()
colors = ['blue',  'maroon', 'fuchsia', 'aqua','red']
sb.violinplot(data=vnats, palette=('Blue',  'Maroon', 'C0','C1','C2'),width=1.0)


#ax1.set_ylim(ymax= 23,ymin=5)
#ax1.set_xlim(xmin=0,xmax=610)
#grid(linestyle="-",linewidth = 2 )

ax1.set_ylabel("Number of Deaths",fontsize=12)
plt.tight_layout()

fig.savefig('a5.png', format='png', dpi=300)
