# 1. Def a new class student
# 2. The class has three attributes, First name, Last name, Undergraduate Programm
# 3. Def a new function that shows the information of a new student

class Student (object):
    def __init__(self,fn,ln,up):
        self.fn=fn
        self.ln=ln
        self.up=up
def show(stu):
    print('His/her full name is '+stu.fn+' '+stu.ln+'. His/her programmm is '+stu.up)
print('For example ')
john=Student('John','West','BMI')
show(john)
print('Now input a new student, his/her ')
a=input('First name is ')
b=input('Last name is ')
c=input("The student's major is ")
ns=Student(a,b,c)
show(ns)