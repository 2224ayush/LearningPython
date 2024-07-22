class Car():
    def __init__(self, color, milage):
            self.color=color
            self.milage= milage
    def __str__(self):
        return(f"The {self.color} car has {self.milage} distance covered")
m=Car("blue",1500)
n=Car("red", 1600)
print(m)
print(n)