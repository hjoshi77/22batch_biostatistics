import numpy as np
import statistics as stat
data=[1,2,2,4,5]
s=np.shape(data)
a=np.mean(data)
d=np.std(data)
b=np.median(data)
c=stat.mode(data)
print ("shape",s)
print ("mean",a)
print ("median",b)
print ("mode",c)
print ("standard deviation",d)


