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

plt.rcParams["axes.labelsize"]=16
plt.rcParams["xtick.labelsize"]=16
plt.rcParams["ytick.labelsize"]=16
plt.rcParams["legend.fontsize"]=16
plt.rcParams['lines.linewidth'] = 2

insurance_filepath = "./insurance.csv"
insurance_data = pd.read_csv(insurance_filepath)
female_bmi = insurance_data[insurance_data['sex'] == 'female']['bmi']
male_bmi = insurance_data[insurance_data['sex'] == 'male']['bmi']

mean_male=np.mean(male_bmi)
error_male=np.std(male_bmi)
mean_female=np.mean(female_bmi)
error_female=np.std(female_bmi)

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,5),sharey=True)


ax1.hist(x=female_bmi,bins=20,density=True,color = "C0")
ax2.hist(x=male_bmi,bins=20,density=True,color="C1")


ax1.set_ylabel("Probability",fontsize=20,fontweight='bold')
ax2.set_xlabel("male_BMI (Kg/m$^{2}$)",fontsize=20,fontweight='bold',color = "C1")
ax1.set_xlabel("Female_BMI (Kg/m$^{2}$)",fontsize=20,fontweight='bold')
## set limit to axis 
ax1.set_xlim(xmax= 60,xmin=10)
ax1.set_ylim(ymax= 0.07,ymin=0)

## Normal fit and plot
mu1, std1 = norm.fit(male_bmi)
mu2, std2 = norm.fit(female_bmi)
x2 = np.linspace(10, 60, 100)
m1 = norm.pdf(x2, mu1, std1)
n1 = norm.pdf(x2, mu2, std2)
print (mu1,std1,mu2,std2) 
ax1.plot(x2, n1, color='red',marker='o',lw=2.0,markersize=8,mfc='white',markevery=10,alpha=1.0);
ax2.plot(x2, m1, color='blue',marker='o',lw=2.0,markersize=8,mfc='white',markevery=10,alpha=1.0);

## Annotate text in the plot
text1= "mean={:.1f} $\pm$ {:.1f}".format(mean_male,error_male)
text2= "mean={:.1f} $\pm$ {:.1f}".format(mean_female,error_female)
ax1.annotate(text1, xy=(35,.06),xytext=(35,0.06),fontsize=16)
ax2.annotate(text2, xy=(35,.06),xytext=(35,0.06),fontsize=16)

plt.tight_layout()
plt.savefig('bmi_bar.png', format='png',bbox_inches='tight',dpi=300)
