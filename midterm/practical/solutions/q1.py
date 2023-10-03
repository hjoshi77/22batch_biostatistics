import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
print("Setup Copltete")
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import matplotlib.dates as mdates 
plt.rcParams["axes.labelsize"]=16
plt.rcParams["xtick.labelsize"]=16
plt.rcParams["ytick.labelsize"]=16
plt.rcParams["legend.fontsize"]=16
plt.rcParams['lines.linewidth'] = 2

filepath = "./WHO-COVID-19-global-data.csv"
data = pd.read_csv(filepath)
usa_y = data[data['Country_code'] == 'US']['New_cases']
usa_x = data[data['Country_code'] == 'US']['Date_reported']
ind_y = data[data['Country_code'] == 'IN']['New_cases']
ind_x = data[data['Country_code'] == 'IN']['Date_reported']
ind1_y = data[data['Country_code'] == 'IN']['Cumulative_cases']
usa1_y = data[data['Country_code'] == 'US']['Cumulative_cases']


fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,5),width_ratios=[10,9])


ax1.plot(ind_x,ind_y,color = "C0",lw=0.5)
ax1.plot(usa_x,usa_y,color = "C1",lw=0.5)
ax2.plot(ind_x,ind1_y,color = "C0",label="India")
ax2.plot(usa_x,usa1_y,color = "C1",label="USA")
leg=plt.legend(handlelength=0.8,fontsize=12,frameon=True)

plt.subplots_adjust(wspace=0, hspace=0)

ax1.set_ylabel("New Cases",fontsize=20)
ax2.set_ylabel("Cumilative Cases",fontsize=20)
## set limit to axis 
ax1.set_xlim(xmax= 1400,xmin=0)
ax2.set_xlim(xmax= 1400,xmin=0)
ax1.set_ylim(ymax= 1000000,ymin=0)
ax2.set_ylim(ymax=109999999,ymin=0)
ax2.xaxis.set_minor_locator(plt.MultipleLocator(30))
ax1.xaxis.set_minor_locator(plt.MultipleLocator(30))
ax1.xaxis.set_major_locator(plt.MultipleLocator(365))
ax2.xaxis.set_major_locator(plt.MultipleLocator(365))
ax1.grid(linestyle="--")
ax2.grid(linestyle="--")
fig.autofmt_xdate()

plt.tight_layout()
plt.savefig('a1.png', format='png',bbox_inches='tight',dpi=300)
