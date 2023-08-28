import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
mpl.rcParams["axes.labelsize"]=16
mpl.rcParams["xtick.labelsize"]=16
mpl.rcParams["ytick.labelsize"]=16
mpl.rcParams["legend.fontsize"]=16
mpl.rcParams['lines.linewidth'] = 2

print("Setup Complete")
insurance_filepath = "./insurance.csv"
insurance_data = pd.read_csv(insurance_filepath)
fig, ax = plt.subplots()
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'],hue=insurance_data['sex'])
ax.set_xlabel("BMI (Kg/m^2)",fontsize=16,fontweight='bold')
ax.set_ylabel("Cost (INR)",fontsize=16,fontweight='bold')

#ax.set_ylim(ymax= 2000,ymin=-50)
#ax.set_xlim(xmax= 180,xmin=0)
plt.savefig('bmi.png', format='png',bbox_inches='tight',dpi=300)

