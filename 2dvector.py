class Vector2D():
    def __init__(self,i,j):
        self.i=i
        self.j=j
        #print("2D vector constructor")
    def display2D(self):
        print(f"2D vector is {self.i}i {self.j}j")
class Vector3D(Vector2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k



    def display3D(self):
        print(f"3D vector is {self.i}i {self.j}j {self.k}k ")
x=Vector3D(2,4,6)
y=Vector2D(3,6)
x.display3D()
y.display2D()
x.display3D()
