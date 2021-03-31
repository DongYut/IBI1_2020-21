# 1. import the apps needed
# 2. read the DNA sequence 3 by 3 and make a re match 
# 3. creat a dictionary that contains code-protein
# 4. from the match take groups and compare to the DNA-Protein graph

import re
seq = 'ATGCGACTACGATCGAGGGCC'
code= re.findall('(\S{3})',seq)
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
Peptide=''
a=''
i=0
while i < len(code) and 'stop' not in a :
    a=(codon[code[i]])
    Peptide=Peptide+a
    i=i+1
    
if 'stop' in a :
    print('The coding stops at code '+str(i)+' in DNA sequence, the stopping code is '+code[i-1]+'.')
print('The sequence is '+seq)
print('The peptide chain is '+Peptide)    