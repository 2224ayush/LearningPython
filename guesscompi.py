import random
num=random.randint(1,100)
print("<-----Player One's Chance----->")
x=int(input("enter your choice between 1 to 100: "))
c=1
while x!=num:
    if num-5<x<num+5:
        print("you are close")
        c+=1
    else:
        print("try again")
        c+=1
    x=int(input("enter your choice: "))
if c==1:
    print("<-----BULLS EYE----->")
print(f"you got it in {c} attempts.")

print("<-----Player Two's Chance----->")
num=random.randint(1,100)
n=int(input("enter your choice between 1 to 100: "))
p=1
while n!=num:
    if num-5<x<num+5:
        print("you are close")
        p+=1
    else:
        print("try again")
        p+=1
    n=int(input("enter your choice: "))
if p==1:
    print("<-----BULLS EYE----->")
print(f"you got it in {p} attempts.")
if c<p:
    print("Player one is the Winner")
else:
    print("Player two is the Winner")
