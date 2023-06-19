s=0
y=0
n=int(input("enter a number"))
while n>0:
    a=n%10
    s=s*10+a 
    n=n//10
if n==s:
    print(s,"is palindrome number")
else:
    print(n,"is not palindrome number")
