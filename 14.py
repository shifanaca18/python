s=0
n=int(input("enter a number"))
while n>0:
    a=n%10
    s=s+a 
    n=n//10
print("Sum :",s)

# n=123
# 123>0
# a=123%10=3 a=3
# s=s+a s=3
# n=n//10=12 n=12

# 12>0
# a=12%10 a=2
# s=s+a s=5
# n=12/10 = 1

# 1>0
# a=1%10  a=1
# s=s+a=6
# n=1/10=0

# 0>0