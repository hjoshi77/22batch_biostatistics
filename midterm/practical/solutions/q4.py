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
from scipy.stats import iqr


plt.rcParams["axes.labelsize"]=16
plt.rcParams["xtick.labelsize"]=16
plt.rcParams["ytick.labelsize"]=16
plt.rcParams["legend.fontsize"]=16
plt.rcParams['lines.linewidth'] = 2

filepath = "./WHO-COVID-19-global-data.csv"
data = pd.read_csv(filepath)
usa = data[data['Country_code'] == 'US'][data.New_deaths > 100]['New_deaths']
ind = data[data['Country_code'] == 'IN'][data.New_deaths > 100]['New_deaths']
bin_usa=int(1394/((2*iqr(usa)/((1364)**(1/3)))))
bin_ind=int(1394/((2*iqr(ind)/((1364)**(1/3)))))
print(bin_usa)
#bin_ind=int(1364/(2*iqr(ind)*((1364)**(1/3))))
bin_usa=40
bin_ind=40
print (bin_usa,bin_ind)

mean_usa=np.mean(usa)
std_usa=np.std(usa)
mean_ind=np.mean(ind)
std_ind=np.std(ind)

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,5),sharey=True)


ax1.hist(x=usa,bins=bin_usa,density=True,color = "C0")
ax2.hist(x=ind,bins=bin_ind,density=True,color="C1")


ax1.set_ylabel("Probability",fontsize=20,fontweight='bold')
ax2.set_xlabel("New Deaths",fontsize=20,fontweight='bold',color = "C1")
ax1.set_xlabel("New Deaths",fontsize=20,fontweight='bold',color='C0')
## set limit to axis 
ax1.set_xlim(xmax= 5000,xmin=10)
ax2.set_xlim(xmax= 5000,xmin=10)

## Normal fit and plot
mu1, std1 = norm.fit(usa)
mu2, std2 = norm.fit(ind)
x2 = np.linspace(0, 1000000, 1000000)
m1 = norm.pdf(x2, mu1, std1)
n1 = norm.pdf(x2, mu2, std2)
print (mu1,std1,mu2,std2) 
ax1.plot(x2, n1, color='red',marker='o',lw=2.0,markersize=8,mfc='white',markevery=1000,alpha=1.0);
ax2.plot(x2, m1, color='blue',marker='o',lw=2.0,markersize=8,mfc='white',markevery=1000,alpha=1.0);

## Annotate text in the plot
text1= "mean={:.1f} $\pm$ {:.1f}".format(mean_usa,std_usa)
text2= "mean={:.1f} $\pm$ {:.1f}".format(mean_ind,std_ind)
ax1.annotate(text1, xy=(2000,.01),xytext=(2000,.01),fontsize=16)
ax2.annotate(text2, xy=(2000,0.1),xytext=(2000,.01),fontsize=16)

plt.tight_layout()
plt.savefig('a4.png', format='png',bbox_inches='tight',dpi=300)
