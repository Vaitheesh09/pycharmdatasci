class Student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        v1 = self.m1 + other.m1
        v2 = self.m2 + other.m2
        s3 = Student(v1,v2)

        return s3
    def __sub__(self, other):
        su1=self.m1 - other.m1
        su2=self.m2 - other.m2
        s4 =Student(su1,su2)

        return s4


s1=Student(75,86)
s2=Student(78,81)

s3=s1+s2

#add = s3.m1 + s3.m2
#print(add)
print(s3.m1)
#s4=s1-s2
#print(s4.su1)
