import matplotlib.pyplot as plt
import numpy as np
import math
(fig,(ax1,ax2)) = plt.subplots(nrows=1,ncols=2,figsize=(18,6))
plt.rcParams["axes.labelsize"]=12
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=120
plt.rcParams["legend.fontsize"]=12
def gamma_function(x):
        return math.gamma(x)  # You can also use scipy.special.gamma(x)


## Bonded Energy
# The Harmonic potential

k1=   1 # Kcal/mol
k2=   2 # Kcal/mol
k3=   3 # Kcal/mol
k4=   4 # Kcal/mol
k5=   100 # Kcal/mol
x_0 = 2   # Angstrom

x = np.linspace(1, 200, 1000)
# Interatomic potential
Y2=(((x)**((k2/2)-1))*np.exp(x*-0.5))/((2**(k2/2))*math.gamma(k2/2))
Y1=(((x)**((k1/2)-1))*np.exp(x*-0.5))/((2**(k2/2))*math.gamma(k2/2))
Y3=(((x)**((k3/2)-1))*np.exp(x*-0.5))/((2**(k2/2))*math.gamma(k2/2))
Y4=(((x)**((k4/2)-1))*np.exp(x*-0.5))/((2**(k2/2))*math.gamma(k2/2))
Y5=(((x)**((k5/2)-1))*np.exp(x*-0.5))/((2**(k2/2))*math.gamma(k2/2))
## Dihedral Angle Energy 
x1 = np.linspace(-5, 5, 500)
n1=2
n2=3

Y6= (gamma_function((n1+1)/2))/((np.sqrt((np.pi)*n1)) * (gamma_function(n1/2)) * ((1 +x1**2)**((n1+1)/2))/n1) 
Y7= (gamma_function((n2+1)/2))/((np.sqrt((np.pi)*n2)) * (gamma_function(n2/2)) * ((1 +x1**2)**((n2+1)/2))/n2) 
line1 = ax1.plot(x, Y1, 'k', lw=2, label='k=1')
line2 = ax1.plot(x, Y2, 'r', lw=2, label='k=2')
line3 = ax1.plot(x, Y3, 'g', lw=2, label='k=3')
line4 = ax1.plot(x, Y4, 'b', lw=2, label='k=4')
line5 = ax1.plot(x, Y5, 'magenta', lw=2, label='k=5')
line6 = ax2.plot(x1, Y6, 'r', lw=1.5, label='n=2')
line7 = ax2.plot(x1, Y7, 'k', lw=1.5, label='n=3')
#ax1.set_xlim(-20, 20)
#ax1.set_ylim(0,1400)
#ax2.set_ylim(0,0.2)
ax2.set_xlim(-5,5)
#plt.ylim(-0.16, 0.8)
ax1.set_ylabel("$\chi^2$ ",fontsize=12)
ax1.set_ylabel("$T-distribution$",fontsize=12)

ax1.grid(linestyle="--")
ax2.grid(linestyle="--")
#plt.ylim(-0.2, 0.3)
ax1.set_xlabel("X", fontsize=12)
#ax2.set_xlabel("Dihedral Angle ($\mathrm{(^{\circ}$))",fontsize=12)
ax2.set_xlabel("X",fontsize=12)

#plt.subplots_adjust(wspace=0, hspace=1)
# Jump through some hoops to get the both line's labels in the same legend:
#lines = line1 + line2 + line3 +line4 
lines = line1 + line2 + line3 + line4 + line5
labels = []
for line in lines:
    labels.append(line.get_label())
ax1.legend(lines, labels)
ax2.legend()
fig.savefig('a6.png', format='png',bbox_inches='tight',dpi=600)

