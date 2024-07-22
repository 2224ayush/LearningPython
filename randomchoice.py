import random
n=int(input("choose one of there"))
x=["Ace","Queen","Jack","King","10"]
print(random.choices(x, weights=[2,7,5,4,8],k=n))

