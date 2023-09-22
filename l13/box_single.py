import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.loadtxt('hes.dat')
fig,ax=plt.subplots()
sns.boxplot(ax=ax,y=data[:,1] )
fig.savefig('box.png', format='png', dpi=300)

