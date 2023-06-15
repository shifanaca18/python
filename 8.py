a=int(input("enter 4 numbers"))
b=int(input())
c=int(input())
d=int(input())
if a>b and a>c and a>d:
    print(a,"is largest number")
elif b>a and b>c and b>d:
    print(b,"is largest number")
elif c>a and c>b and c>d:
    print(c,"is largest number")
else:
    print(d,"is largest number")