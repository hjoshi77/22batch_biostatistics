import matplotlib.pyplot as plt
import numpy as np
(fig,(ax1,ax2)) = plt.subplots(nrows=1,ncols=2,figsize=(18,6),width_ratios=[1, 2])
plt.rcParams["axes.labelsize"]=12
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["legend.fontsize"]=12

## Bonded Energy
# The Harmonic potential

k2=   3.0 # Kcal/mol
k1=   1.5 # Kcal/mol
x_0 = 2   # Angstrom

x = np.linspace(-20, 20, 1000)
# Interatomic potential
Y2=k2*((x-x_0)**2)
Y1=k1*((x-x_0)**2)
## Dihedral Angle Energy 
phi = np.linspace(0, 360, 500)
k=0.1
delta=180
n1=2
n2=3

Y3= k*(1+np.cos(((n1*phi)-delta)*(np.pi/180)))
Y4= k*(1+np.cos(((n2*phi)-delta)*(np.pi/180)))
line1 = ax1.plot(x, Y1, 'k', lw=2, label='k=1.5')
line2 = ax1.plot(x, Y2, 'r', lw=2, label='k=3')
line3 = ax2.plot(phi, Y3, 'r', lw=1.5, label='n=2')
line4 = ax2.plot(phi, Y4, 'k', lw=1.5, label='n=3')
ax1.set_xlim(-20, 20)
ax1.set_ylim(0,1400)
ax2.set_ylim(0,0.2)
ax2.set_xlim(0,360)
#plt.ylim(-0.16, 0.8)
ax1.set_ylabel("Energy ($\mathrm{kcal/mol}$)",fontsize=12)
ax1.grid(linestyle="--")
ax2.grid(linestyle="--")
#plt.ylim(-0.2, 0.3)
ax1.set_xlabel("Interatomic distance ($\mathrm{\AA}$)",fontsize=12)
#ax2.set_xlabel("Dihedral Angle ($\mathrm{(^{\circ}$))",fontsize=12)
ax2.set_xlabel("Dihedral Angle ($^\circ$)",fontsize=12)

#plt.subplots_adjust(wspace=0, hspace=1)
# Jump through some hoops to get the both line's labels in the same legend:
lines = line1 + line2 
labels = []
for line in lines:
    labels.append(line.get_label())
ax1.legend(lines, labels)
ax2.legend()
fig.savefig('a6.png', format='png',bbox_inches='tight',dpi=600)

