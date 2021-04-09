# 1. Read file and import os and re
# 2. Firstly find the name part (starts with >)
# 3. Make the sequnce in one line
# 4. Find 'unknown function' DNA and write into new file
# 5. Rewrite the title of DNA 

import os 
import re
os.chdir('Practical8')
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as f:
  read = f.read()
  read = read.replace('\n','').replace('>','\n>')        # make sequce in one line
gene=open('unknown_function.fa','w')
gene.write(read)
gene.close
f.close
g=open('unknown_function.fa','r')
output=''
for line in g:
    if 'unknown' in line:
        output=output + line
g.close
rewrite=open('unknown_function.fa','w')     # create new file and write for first time
rewrite.write(output)
rewrite.close
rewrite=open('unknown_function.fa','r')
output2=''
length=[]
count=''
for line in rewrite:
      count=re.sub(r'.+]','',line)              
      sep=re.sub(r']',r'\n',line)
      length.append(len(count))
      output2= output2+ sep               # find the length of target DNA and save them in a list
rewrite.close
rewrite2=open('unknown_function.fa','w')
rewrite2.write(output2)
rewrite2.close
rewrite3=open('unknown_function.fa','r')
z=0
name2=''
output3=''
for line in rewrite3:
    if 'unknown' in line:
        name=re.search(r'gene:(\S+)',line)                       # combine the new title in front of target DNA
        name2=name.group(1)+'      '+str(length[z]-1)
        z=z+1
        title=re.sub(r'.+',name2,line)
    else:
        if 'T' in line:
          
          output3=output3+title+line
final=open('unknown_function.fa','w')                        # write the file for second time 
final.write(output3)


       

