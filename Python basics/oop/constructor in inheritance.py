class A:
    def __init__(self):
        print("In A init")
    def feature1(self):
        print("Feature 1 running")
    def feature2(self):
        print("Feature 2 running")

class B(A):
    def __init__(self):
        super().__init__()
        print("In B init")
    def feature3(self):
        print("Feature 3 running")
    def feature4(self):
        print("Feature 4 running")


a1=B()