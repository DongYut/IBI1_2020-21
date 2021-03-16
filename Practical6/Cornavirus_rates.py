# 1. make a dic including cases
# 2. define lables, explode, sizes
# 3. draw a pie diagram

import matplotlib.pyplot as plt
dic={'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
sum= dic['USA']+dic['India']+dic['Brazil']+dic['Russia']+dic['UK']
labels='USA','India','Brazil','Russia','UK'
sizes=[100*dic['USA']/sum,100*dic['India']/sum,100*dic['Brazil']/sum,100*dic['Russia']/sum,100*dic['UK']/sum]
explode=(0,0.1,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()







