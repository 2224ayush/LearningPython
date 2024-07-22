n=int(input("Enter number"))
a=-1
b=1
i=1
while(i<=n):
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)
    
