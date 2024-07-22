'''for i in range(0,6):
    for j in range(0,i+1):
        print("*",end=" ")
    print()'''
'''for i in range(5):
    for j in range(i,5):
        print("*",end=" ")
    print()'''
"""for i in range(5):#kinda brutforce
    for j in range(i,5):
        print(" ", end=" ")
    for k in range(5,i+6):
        print("*", end=" ")
    print()
    #corrected
for i in range(5):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()"""
#pyramid
"""for i in range(6):
    for j in range(i,7):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*", end=" ")
    for l in range(0,i):
        print("*", end=" ")
    print()
#inverted pyramid
for i in range(7):
    for j in range(0,i+1):
        print(" ",end=" ")
    for k in range(i,7):
        print("*", end=" ")
    for l in range(i,6):
        print("*",end=" ")
    print()"""
"""for i in range(5):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*", end=" ")
    for l in range(1,i+1):
        print("*", end=" ")
    print()
for i in range(4):
    for j in range(0,i+2):
        print(" ", end=" ")
    for k in range(i,4):
        print("*", end=" ")
    for l in range(i,3):
        print("*",end=" ")
    print()"""
for i in range(5):
    for j in range(i,4):
        print(" ", end=" ")
    for k in range(0,i+1):
        print("*", end=" ")
    for l in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(4):
    for j in range(0,i+1):
        print(" ", end=" ")
    for k in range(i+1,5):
        print("*", end=" ")
    for l in range(i+1,4):
        print("*", end=" ")
    print()

