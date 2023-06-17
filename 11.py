a=0
b=1
s=1
print(a)
print(b)
for c in range(2,6):
    n=a+b
    s=s+n
    a=b 
    b=n
    print(n)
print("sum",s)

