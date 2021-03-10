# 1.define rate of infection r
# 2.calculate the new infected individuals
# 3.calculate whole number of infectors in a round
# 4.loop the round 5 times and output the result 

r= 1.2
n=84
for i in range (1,6):
   n=n+ r*n
print("After 5 rounds infection,the number of patients will be "+str(n))

