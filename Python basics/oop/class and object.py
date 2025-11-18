
class MyComputer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("confic",self.cpu,self.ram)

com1=MyComputer('i7',16)#-->object creation
com2=MyComputer('i5',8)
#MyComputer.config(com1)

com1.config()#object itself call the method
com2.config()