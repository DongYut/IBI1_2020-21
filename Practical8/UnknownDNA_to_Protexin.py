# 1.Import os and re, save the dic of DNA-Protein
# 2.Define the funtion of translating DNA as a new command
# 3.Same as previous work read the target DNA
# 4.Translate them and store in a new document (the name is 'input')


import os 
import re
codon = {'ATA':'J', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'B', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Z',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'O(stop)', 'TAG':'U(stop)',
    'TGC':'C', 'TGT':'C', 'TGA':'X(stop)', 'TGG':'W'}
def dp(seq):
    code= re.findall('(\S{3})',seq)
    Peptide=''
    a=''
    i=0
    while i < len(code) and 'stop' not in a :
        a=(codon[code[i]])
        Peptide=Peptide+a
        i=i+1
    return Peptide                         # define a new function to translate
os.chdir('Practical8')
fn=input('The name of file is (do not contain file type): ')+'.fa'
print('The name of file will be '+fn)
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as f:
  read = f.read()
  read = read.replace('\n','').replace('>','\n>')
gene=open(fn,'w')
gene.write(read)
gene.close
f.close
g=open(fn,'r')
output=''
for line in g:
    if 'unknown' in line:
        output=output + line
g.close
rewrite=open(fn,'w')
rewrite.write(output)
rewrite.close
rewrite=open(fn,'r')
output2=''
length=[]
count=''
for line in rewrite:
      count=re.sub(r'.+]','',line)
      sep=re.sub(r']',r'\n',line)
      length.append(len(count))
      output2= output2+ sep
rewrite.close
rewrite2=open(fn,'w')
rewrite2.write(output2)
rewrite2.close
rewrite3=open(fn,'r')
z=0
name2=''
output3=''
for line in rewrite3:
    if 'unknown' in line:
        name=re.search(r'gene:(\S+)',line)
        name2=name.group(1)+'      '+str((length[z]-1)/3)
        z=z+1
        title=re.sub(r'.+',name2,line)
    else:
        if 'T' in line:
          line=dp(line)+'\n'                     # all same as previous work, but add this line to translate DNA
          output3=output3+title+line
final=open(fn,'w')
final.write(output3)
final.close
