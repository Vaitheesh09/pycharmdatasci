# Types of Methods

class Student:
    school='TDTA'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self): # instance method
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):# accessor method
        return self.m1

    def set_m1(self,value):#mutator
        self.m1=value
        return self.m1
    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def stu_info():
        print("This is Student class...")

s1=Student(76,85,84)
s2=Student(98,67,98)

print(s1.avg())
print(s1.get_m1())
print(s1.set_m1(80))

print(Student.info())
print(Student.stu_info())