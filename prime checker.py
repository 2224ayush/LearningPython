#Write a program to check if a number, entered by the user, is prime or no
x=int(input("enter number"))
for i in range(2,x):
    if(x%i==0):
        print(f"{x} is not prime")
        break
else:
    print(f"{x} is prime")