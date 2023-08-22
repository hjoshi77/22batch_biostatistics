import numpy as np
import statistics as stat
data=np.loadtxt('inside_hst.dat')
s=np.shape(data)
a=np.mean(data[:,1])
b=np.median(data[:,1])
c=stat.mode(data[:,1])
print ("shape",s)
print ("mean",a)
print ("median",b)
print ("mode",c)


