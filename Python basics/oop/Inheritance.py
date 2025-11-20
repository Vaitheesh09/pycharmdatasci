class A:
    def feature1(self):
        print("Feature 1 running")
    def feature2(self):
        print("Feature 2 running")

class B(A):
    def feature3(self):
        print("Feature 3 running")
    def feature4(self):
        print("Feature 4 running")

a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature2()
