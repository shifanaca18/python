def add():
    global a
    a=input("Enter a name ")
    global b
    b=int(input("rate of Intrst :"))
    global c
    c=int(input("amount"))
    global d
    d=int(input("number of year")) 
def intrest():
    global e
    e=c*b/100
    print("intrest",e)
def emi():
    f=c+(e*d)
    g=f/(d*12)
    print("emi",g)

add()
intrest()
emi()