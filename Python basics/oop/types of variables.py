class car:
    Wheel=4 #static or class variable
    def __init__(self,brand,color):
        self.brand=brand #instance variable -its ch
        self.color=color #instance variable

c1=car('BMW','silver')
c2=car('Thar','black')
c1.brand='Benz'
c1.Wheel=6
print(c1.brand,c1.color,c1.Wheel)
print(c2.brand,c2.color,c2.Wheel)