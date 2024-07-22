    """class quitError(Exception):
    "raised when user enters trying in int except quit"
    pass
x=input("choose a number between 1 to 9 or quit:")
if x.isdigit() and 1<int(x)<9:
    print(x)
elif x=="quit":
    print(x)
else:
    raise quitError("qrrorasd")"""
class SingleError(Exception):
    pass
x=input("enter relationship status: ")
if x.lower()=="single":
    raise SingleError("koi ni bhai sbka ktegaaa but for now, you can't access this program")
else:
    print("smiles in pain")
