class Calculation:
    def data(self):
        global a
        a=int(input("Enter 2 Number"))
        global b
        b=int(input())
    def sum(self):
        c=a+b
        print("Sum",c)
    def sub(self):
        d=a-b
        print("Sub :",d)
    def multy(sub):
        e=a*b
        print("Multy :",e)
    def div(self):
        f=a/b
        print("Div :",f)
s=Calculation()
s.data()
s.sum()
s.sub()
s.multy()
s.div()