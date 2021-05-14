import xml.dom.minidom
from xml.dom.minidom import parse
DOM= xml.dom.minidom.parse("go_obo.xml")
collection = DOM.documentElement
terms= collection.getElementsByTagName('term')        #Read the file and make a DOM tree
dics={}
for term in terms:
    ids=term.getElementsByTagName('id')
    dics[ids[0].firstChild.data]=[]
for term in terms:
    list=[]
    ids=term.getElementsByTagName('id')
    is_as=term.getElementsByTagName('is_a')
    for is_a in is_as:
        dics[is_a.firstChild.data].append(ids[0].firstChild.data)
    dics[ids[0].firstChild.data]=list
def count(b):               #Define a new function to count the childnode number
    for i in range(len(b)):                      # b is the list  from next function, the first-level childnode of XX-assosiated
        if len(dics[b[i]])==0:
            if b[i] not in listf:            #This is to prevent reptition of same childnode GO:XXXXXX
                listf.append(b[i])                 #If a first-level childnode doesn't have childnode, then simply add it into the listf
        else:
            if b[i] not in listf:                 
                listf.append(b[i])
            count(dics[b[i]])                 #If a first-level childnode have childnode, then repete the function itself, to count all the childnodes.
    return len(listf)             #The length of listf will be the number of childnodes

def countnumb(a):
    for term in terms:                     #Get the element 'term'
        defstr=term.getElementsByTagName('defstr')      #From term get element 'defstr'          
        if a in defstr[0].firstChild.data:
            idss=term.getElementsByTagName('id')
            lists=dics[idss[0].firstChild.data]                #From the dics read the first-level childnode of XX-assosiated.
            n=count(lists)                #Use the function above to make the listf. The Listf consists of all the GO:XXXXX term that is the chidnodes of XX-assosiated term.
    print('The childnode number of '+a+' is '+ str(n)+'.')           
    return n
listf=[]          # Everytime count the childnode, the listf should be cleaned.
DNA=countnumb('DNA')
listf=[]
RNA=countnumb('RNA')
listf=[]
Protein=countnumb('protein')
listf=[]
CH=countnumb('carbohydrate')             # I am interested in carbohydrate


import matplotlib.pyplot as plt
dic={'DNA':DNA,'RNA':RNA,'Protein':Protein,'Carbohydrate':CH}
sum= dic['DNA']+dic['RNA']+dic['Protein']+dic['Carbohydrate']       # the sum of all cases
labels='DNA','RNA','Protein','Carbohydrate'
sizes=[100*dic['DNA']/sum,100*dic['RNA']/sum,100*dic['Protein']/sum,100*dic['Carbohydrate']/sum]    # the percentage of cases is count by "100*X/sum"
explode=(0,0.1,0,0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title('The childNodes number of different molequle-assosiated terms.')
plt.show()        # make the plot and draw
