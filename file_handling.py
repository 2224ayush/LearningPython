"""with open("abc.txt", "a") as fobj:
    x=input("what you want to add? ")
    fobj.write(f"{x}\n")"""
"""ls=[]
with open("abc.txt") as fobj:
    for names in fobj:
        ls.append(names)
for i in sorted(ls):
    print("hello, ",i.strip())"""
"""with open("hello.csv","r") as fobj:
    m=fobj.read()
    n= m.rstrip()
    print(n.split(","))"""
"""with open("hello.csv","r") as fobj:
    for line in fobj:
        row=line.strip().split((","))
        print(row[0],"is", row[1])"""
"""ls=[]
with open("hello.csv") as fobj:
    for lines in fobj:
        name,house = lines.rstrip().split(",")
        ds={"name": name , "house":house }
        ls.append(ds)
def keyss(lt):
    return lt["name"]
for i in sorted(ls,key=keyss):
    print(f"{i['name']} is in {i['house']}")"""
"""import segno
qr= segno.make_qr("https://www.pornhub.com")
n=qr.save("youtubeqr.png")"""
"""
import csv
name = input("enter name: ").rstrip()
house = input("enter house: ").rstrip()
with open("hello.csv", "a") as fobj:
    writer = csv.DictWriter(fobj,fieldnames=["name","house"])#dict writer ke sath hume fieldnames mai list pass krni hoti hai apne column names ki
    writer.writerow({"name":name,"house":house})"""