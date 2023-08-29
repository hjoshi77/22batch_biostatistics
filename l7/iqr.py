# Import the numpy library as np
import numpy as np
  
data = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 
        101, 105, 112, 116]
  
# First quartile (Q1)
Q1 = np.median(data[:10])
  
# Third quartile (Q3)
Q3 = np.median(data[10:])
  
# Interquartile range (IQR)
IQR = Q3 - Q1
  
print(IQR)
