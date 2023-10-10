import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from scipy.stats import iqr
import seaborn as sns
print("Setup Copltete")
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import statistics as stat

##f = open("a3.txt", "w") 
filepath = "./WHO-COVID-19-global-data.csv"
data = pd.read_csv(filepath)
usa = data[data['Country_code'] == 'US']['New_deaths']
ind = data[data['Country_code'] == 'IN']['New_deaths']

mod_usa_data=data[data['Country_code'] == 'US'] [data.New_deaths > 0]['New_deaths']
mod_ind_data=data[data['Country_code'] == 'IN'] [data.New_deaths > 0]['New_deaths']
##print (mod_usa_data)

mean_usa=np.mean(usa)
median_usa=np.median(usa)
mod_usa=stat.mode(mod_usa_data)
std_usa=np.std(usa)
iqr_usa=iqr(usa)

print ("USA")
print ("Mean", mean_usa)
print ("Median", median_usa)
print ("Mode", mod_usa)
print ("Standard Deviation", std_usa)
print ("IQR ", iqr_usa)

mean_ind=np.mean(ind)
median_ind=np.median(ind)
mod_ind=stat.mode(mod_usa_data)
std_ind=np.std(ind)
iqr_ind=iqr(ind)

print ("India")
print ("Mean", mean_ind)
print ("Median", median_ind)
print ("Mode", mod_ind)
print ("Standard Deviation", std_ind)
print ("IQR ", iqr_ind)

#file1.close()
