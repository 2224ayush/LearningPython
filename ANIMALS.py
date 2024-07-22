class Animals():
    def __init__(self):
        print("animal constructor")
class Pets(Animals):
    def __init__(self):
        print("pets constructor")
class Dog(Pets):
    def __init__(self,name):
        self.name=name
        pass
    def bark(self):
        print(f"{self.name} does bhao bhao")
x=Dog("tuffie")
x.bark()