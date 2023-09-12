import matplotlib.pyplot as plt
import numpy as np
import scipy 
from scipy import stats
mat=np.loadtxt("score.data")
fig,ax = plt.subplots()
ax.set_ylabel("Score ",fontsize=12)
ax.set_xlabel("Hours studied ",fontsize=12)
s=50
coef=np.polyfit(mat[0:,0],mat[0:,1], 1) 
r = np.corrcoef(mat[0:,0],mat[0:,1])
p= scipy.stats.pearsonr(mat[0:,0],mat[0:,1]) 
print (" Pearson correlation coefficint ",p)
slope, intercept, r, p, stderr=scipy.stats.linregress(mat[0:,0],mat[0:,1])
print (coef)
#print (fit)
poly1d_fn = np.poly1d(coef)
plt.scatter(mat[0:,0], mat[0:,1],s)
plt.plot(mat[0:,0],poly1d_fn(mat[0:,0]),color='C1',linestyle='--')
fig.savefig('plot.png', format='png',bbox_inches='tight',dpi=300)

