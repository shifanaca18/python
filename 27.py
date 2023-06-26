name=['A','B','C','D']
n=int(input("enter a number"))
if n==1:
    name.append(input("enter a name"))
    print(name)
elif n==3:
    a=input("enter name")
    if a in name:
        del name[name.index(a)]
        print("Delleted Success")
        print(name)
    else:
        print("Data not available")
        print(name)
if n==2:
    b=input("enter name")
    if b in name:
        c=input("enter edited name")
        name[name.index(b)]=c
        print(name)
    else:
        print("name not valid")

