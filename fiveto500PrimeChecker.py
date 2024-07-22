for i in range(5,501):
    for j in range(2,i):
        if(i%j)==0:
            break
    else:
        print(i, end=",")
