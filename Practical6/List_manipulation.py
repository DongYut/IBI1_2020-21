# 1. import matplotlinb
# 2. make two lists
# 3. make third list contains average exon lengths
# 4. make the plot and show

import matplotlib.pyplot as plt
import numpy as np
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts=np.array([51,1142,42,216,25,650,32533,57,1,523])    # define two number list that can be calculated
AV_exon_lengths=gene_lengths/exon_counts
AV_exon_lengths.sort()     # calculate average lenghts and make a list and sort
print("The sorted average exon lengths list is "+str(AV_exon_lengths))
plt.boxplot(AV_exon_lengths,sym='*',vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=True,boxprops = {'color':'orangered','facecolor':'pink'})
plt.title("Average exon lengths distrubution")
plt.xlabel("Exon Lengths")
plt.ylabel("List 1")                       # do some diy to the plot
plt.show()


