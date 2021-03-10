# 1.define varibles as first two number
# 2.calculate the next two number
# 3.run the calculation 5 times and there will be 12 numbers
# 4.calculate 13th number

a= 1
b= 1
print(a)
print(b)
for i in range (1,6):      # run 5 times
  a=a+b
  print(a)
  b=a+b
  print(b)
a= a+b                     # 13th number 
print(a)
   
   
   
