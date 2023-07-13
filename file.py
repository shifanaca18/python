a=int(input("Enter a number"))
if a==1:
    for i in range(1):
        b=input("Enter a name")
        file=open("shifana.txt","a")
        file.write("\n"+b)
        print("adding suucessfully")
if a==2:
    c=input("Enter a name")
    file=open("shifana.txt","r")
    sho=file.read()
    li=list(sho.split("\n"))
    if c in li:
        print("Enterd Name is in list")
    else:
        print("Invalid")
if a==3:
    d=input("Enter a name")
    file=open("shifana.txt","r")
    sho=file.read()
    li=list(sho.split("\n"))
    if d in li:
        del li[li.index(d)]
        print("deletd succesdfully")
        print(li)
        st='\n'.join(map(str,li))
        file=open("shifana.txt","w")
        file.write(st)
    else:
        print("data not found")
if a==4:
    e=input("enter a name")
    file=open("shifana.txt","r")
    edit=file.read()
    li=list(edit.split("\n"))
    if e in li:
        name=input("enter edited name")
        li[li.index(e)]=name
        st='\n'.join(map(str,li))
        file=open("shifana.txt","w")
        file.write(st)
        print(name," writing successfully")
    else:
        print("not found")

