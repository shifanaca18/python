name=['A','B','C','D']
n=int(input("enter a number"))
# if n==1:
#     name.append(input("enter a name"))
#     print(name)

# elif n==2:
#     a=(input("enter name"))
#     del name
#     print(name)
if n==3:
    name=['A','B','C','D']
    b=(input("enter name"))
    if b in name:
        input("enter edited name")
        name[b]=b
    print(b)


