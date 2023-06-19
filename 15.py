s=0
n=int(input("enter a number"))
while n>0:
    a=n%10
    s=s*10+a 
    n=n//10
print(s)