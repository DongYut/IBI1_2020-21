

import os 
import re
os.chdir('Practical8')
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as f:
  read = f.read()
  read = read.replace('\n','').replace('>','\n>')
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
rewrite=open('unknown_function.fa','w')
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
      output2= output2+ sep
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
        name=re.search(r'gene:(\S+)',line)
        name2=name.group(1)+'      '+str(length[z]-1)
        z=z+1
        title=re.sub(r'.+',name2,line)
    else:
        if 'T' in line:
          
          output3=output3+title+line
final=open('unknown_function.fa','w')
final.write(output3)


       

