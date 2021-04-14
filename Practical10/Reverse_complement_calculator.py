# 1. Import applications
# 2. Read the DNA sequence and make it reverse
# 3. Change all the lower case to upper case
# 4. Change as A-T and C-G make a complement sequnece.4
seq='ATCGGAGGCgtgtAaT'
print('The example sequence is "ATCGGAGGCgtgtAaT"')
def transfer(seq):
    trans={'A':'T','a':'T','C':'G','c':'G','G':'C','g':'C','T':'A','t':'A'}
    lis= list(seq)[::-1]
    i=0
    comple=''
    while i < len(lis):
        comple=comple+trans[lis[i]]
        i=i+1
    print('The reverse complement sequence is '+comple)
    return comple
transfer(seq)
seq=input('The new DNA sequence is ')
transfer(seq)