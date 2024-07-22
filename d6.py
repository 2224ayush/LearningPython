"""def outerFunction(text):
    def innerFunction():
        print(text)
    return innerFunction
myfunc=outerFunction("Ayush")
myfunc()
"""
"""def xyz():
    count=0
    def coy():
        nonlocal count
        count+=1
        return count
    return coy
p1=xyz()

print(p1())
print(p1())
print(p1())
print(type(xyz()))

print(type(p1()))"""
"""
def xyz():
    print('hello')
def decor(mn):
    mn()
    print('how are you')
decor(xyz)
"""
"""def decor(xyz):
    def inner():
        xyz()
        print('ayush')
    return inner
@decor
def xyz():
    print("hello")
xyz()"""
"""def decor1(addn):
    def inner():
        res=addn()
        n4=int(input("enter num4: "))
        res-=n4
        return res
    return inner
def decor(addn):
    def inner():
        res=addn()
        n3=int(input("enter num3: "))
        res+=n3
        return res
    return inner

@decor1
@decor
def addn():
    num1=int(input("enter num1: "))
    num2=int(input("enter num2: "))
    res=num1+num2
    return res
print(addn())"""
"""def decor(name):
    def inner():
        print('*'*10)
        print(name())
        print('*' * 10)
    return inner
@decor
def name():
    x="ayush"
    return x
name()"""
#write a decorator that print start before a function is called and end after the function is called
"""def decor(mnc):
    def inner():
        print("start")
        print(mnc())
        print("end")
    return inner
@decor
def mnc():
    return "google"
mnc()"""
#write a decorator that prints the 4 times of the og number and after that it prints the sq of that num
"""def decor(func):
    def inner():
        cx=func()
        px=cx*4
        print(f"four times of {cx} is {px}")
        sx=px*px
        print(f"square of {px} is {sx}")
    return inner
@decor
def func():
    nx=int(input("enter number: "))
    return nx
func()"""
#iterator
"""ls=[10,20,30,50,40] 
x=iter(ls)
y="python"
z=iter(y)
print(id(z))
print(type(z))
print(dir(z))
print(type(x))
print(dir(x))
print(dir(z)==dir(x ))
print(next(z))
print(next(z))
print(next(x))
print(next(x))"""
"""
class xyz():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
p=xyz()
myiter=iter(p)
print(myiter)
p.
.0rint(next(myiter))
0pr 2345/int(next(myiter))
print(next(myiter))
"""
"""def xyz(z):
    while(z>0):
        if z%2==0:
            yield "even"
        else:
            yield "odd"
        z-=1
for i in xyz(7):
    print(i)"""
from tkinter import *
root=Tk()
root.title("hello world")
root.geometry('200x200')
root.mainloop()

