import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
plt.rcParams["axes.labelsize"]=16
plt.rcParams["xtick.labelsize"]=16
plt.rcParams["ytick.labelsize"]=16
plt.rcParams["legend.fontsize"]=16
plt.rcParams['lines.linewidth'] = 2

print("Setup Copltete")
insurance_filepath = "./insurance.csv"
insurance_data = pd.read_csv(insurance_filepath)
fig, ax = plt.subplots()
sns.scatterplot(x=insurance_data['age'], y=insurance_data['charges'])
coef=np.polyfit(insurance_data['age'], insurance_data['charges'],1)
poly1d_fn = np.poly1d(coef) 
plt.plot(insurance_data['age'],poly1d_fn(insurance_data['age']),color='C1',linestyle='--')
r = np.corrcoef(x=insurance_data['age'], y=insurance_data['charges'])

p= scipy.stats.pearsonr(x=insurance_data['age'], y=insurance_data['charges'])
print (" Pearson correlation coefficint ",p)
print (" Numpy correlation coefficint ",r)

ax.set_xlabel("Age (Year)",fontsize=16,fontweight='bold')
ax.set_ylabel("Insurnce cost (INR)",fontsize=16,fontweight='bold')

#ax.set_ylim(ymax= 2000,ymin=-50)
#ax.set_xlim(xmax= 180,xmin=0)
plt.savefig('age_vs_charge.png', format='png',bbox_inches='tight',dpi=300)

