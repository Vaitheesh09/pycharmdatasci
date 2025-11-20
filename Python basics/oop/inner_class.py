class Student:
     def __init__(self,name,rollno):
         self.name=name
         self.rollno=rollno
         self.lap=self.Laptop()

     def show(self):
         print(f"The student name is {self.name} and Rollnumber is :{self.rollno}")
         self.lap.show()

     class Laptop:
         def __init__(self):
             self.brand='Asus'
             self.cpu='i7'
             self.ram='16gb'
             self.storage='1TB'

         def show(self):
             print(self.brand,self.cpu,self.ram)


s1=Student('vaithi',108)
s2=Student('jeni',572)
s1.show()

lap1=s1.lap
#print(lap1.brand)
#lap3=Student.Laptop()
#print(lap3.cpu)
lap1.show()

