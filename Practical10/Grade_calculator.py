# 1. Def a new class student
# 2. The class has four attributes, Name, code portfolio grades, presentation grades, final exam grades
# 3. Def a new function that calculate and show the student's final grade
class Student (object):
    def __init__(self,n,cp,pp,fe):
        self.n=n
        self.cp=cp
        self.pp=pp
        self.fe=fe
def getfinal(stu):
    fn=stu.cp*0.4+stu.pp*0.3+stu.fe*0.3
    print(stu.n+"'s final grade is "+str(fn)+'.')
print("For example, John West's code portfolio is 80,  his pre is 78 and final exam is 86 ")
john=Student('John west',80,78,60)
getfinal(john)
print('Now input a new student.')
a=input('His/her name is ')
b=input('His/her code portfolio is ')
c=input("His/her presentation grade is ")
d=input('His/her final exam grade is ')
ns=Student(a,int(b),int(c),int(d))
getfinal(ns)
