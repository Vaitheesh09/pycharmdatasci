class Pycharm:
    def execute(self):
        print("Compling")
        print("Running")

class Mycharm:
    def execute(self):
        print("Spell Check")
        print("Compling")
        print("Running")

class Laptop:
    def code(self,ide,ide1):
        ide.execute()
        ide1.execute()

ide=Mycharm()
ide1=Pycharm()
#ide=Pycharm()
lap1=Laptop()
lap1.code(ide,ide1)
#print(type(ide))
