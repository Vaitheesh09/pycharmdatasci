class computer:
    def __init__(self):
        self.name="vaitheesh"
        self.age=21
    def update(self):
        self.name='Lijin'
    def compare(self,other):
        return self.age == other.age

c1=computer()
c2=computer()

c1.name='jes'
c1.age=21
if c1.compare(c2):
    print("they are same")
else:
    print("They are diff")
c1.update()
print(c1.name)
print(c2.age)