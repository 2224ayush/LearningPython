#ENUMERATE
x=[10,20,40,80,160]
for index, items in enumerate(x):
    print(f"{items} is at index {index} ")
#LIST COMPREHENSION-> way to create list on existing list.

#normal way
x1=[10,20,40,80,160]
ls=[]
for i in x1:
    i=i*i
    ls.append(i)
print(ls)
#via list comprehension
x2=[10,20,40,80,160]
sqls=[i*i for i in x2]
print(sqls)