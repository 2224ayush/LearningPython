#types are used to define explicitly the type of variable
#which is used to access operation recommendations related to the declared type
n:str="ayush"
print(n.capitalize())
#major use in function
def add(a:int,b:int) -> int:
    return(a+b)
print(add(10,9))
from typing import List,Tuple
num : List[int]=[10,20,25,50]
print(num)
alnum:Tuple[int,str]=(10,"ayush")
print(alnum)