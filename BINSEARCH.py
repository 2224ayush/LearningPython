#Write a program that searches for a number in a list and stops when it finds the
#number using the break statement.
#binary search
def main():
    ls=[1,2,2,1,5,3,6,4,99,8,7,9,11]
    ls.sort()
    target=99
    z=binsearch(ls,target)
    print(z)
def binsearch(lst,target):
    start=0
    end=len(lst)
    while(start<=end):
        mid=round(start+(end-start)/2)
        if(lst[mid]<target):
            start=mid+1
        elif(lst[mid]>target):
            end=mid-1
        else:
            return mid
    return mid

main()