#walrus operator gives to compatibility to store a value in a variable inside a conditional
if (n:=len([10,20,30,40,50])>3):
    print("list is too long")
print(n)
# the output of n will be either true or false as per the condition