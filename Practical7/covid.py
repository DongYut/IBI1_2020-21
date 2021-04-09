# 1. Read the file and import apps
# 2. Choose the column that starts with Afghanistan
# 3. Create new cases that has data 'World'
# 4. Do the task work follow the guide

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

covid_data=pd.read_csv("full_data.csv")
print("All columns and every second row between 0 and 10")
print(covid_data.iloc[0:11:2,:])            # to show all columns and every second row between 0 and 10
print(" ")
my_column=[]
for i in range(0,7996):
  a= covid_data.iloc[i,1]=="Afghanistan"    # to compute a Boolean
  my_column.append(a)                       # make the boolean list for reading the data

print("All rows corresponding to Afghanistan")
print(covid_data.iloc[my_column,:])         # to show rows corresponding to Afghanistan


my_column=[]
for i in range(0,7996):
  a= covid_data.iloc[i,1]=="World"
  my_column.append(a)
world_new_cases= covid_data.iloc[my_column,[True,False,True,True,False,False]]
print("The mean of new cases around the world is ")
print(world_new_cases["new_cases"].mean())     # compute and show the mean of world new cases
print("The median of new cases around the world is ")
print(world_new_cases["new_cases"].median())

plt.figure()
plt.boxplot(world_new_cases["new_cases"],sym='*',vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False,boxprops = {'color':'orangered','facecolor':'pink'})
plt.ylabel('Counts')
plt.xlabel('New Cases')
plt.title('New cases boxplot')
print("Now shows the boxplot of new cases around the world")              # make Figure1 the boxplot of new cases

plt.figure()
plt.plot(world_new_cases["date"],world_new_cases["new_cases"],'yo',label='Cases')
plt.plot(world_new_cases["date"],world_new_cases["new_deaths"],'ro',label='Deaths')
print("Now shows the plot of dates and new cases and new deaths")
plt.ylabel('Counts')
plt.xlabel('Dates')
plt.title('New deaths and cases around the world')
plt.legend()
plt.xticks(world_new_cases["date"].iloc[0:len(world_new_cases["date"]):4],rotation=-90)
plt.show()                # make Figure2 the plot of dates and new cases and new deaths and show two figures

# Question: At 2020-03-31, how difference is the propotion of death in China to that in US? Why?
# From this line the question will be discussed.
my_column=[]
for i in range(0,7996):
  a= (covid_data.iloc[i,1]=="China") and (covid_data.iloc[i,0]=="2020-03-31")
  my_column.append(a)
china= covid_data.iloc[my_column,:]
my_column=[]
for i in range(0,7996):
  a= (covid_data.iloc[i,1]=="United States") and (covid_data.iloc[i,0]=="2020-03-31")
  my_column.append(a)
US= covid_data.iloc[my_column,:]
ChinaP= np.array(china["total_deaths"])/np.array(china["total_cases"])
print("The proportion of deaths in China is")
print(ChinaP)
USP= np.array(US["total_deaths"])/np.array(US["total_cases"])
print("The proportion of deaths in US is")
print(USP)
