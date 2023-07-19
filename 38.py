class First:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        self.c=self.a+self.b
        print("sum",self.c)

    def mul(self):
        self.d=self.a*self.b
        print("multy",self.d)
    def div(self):
        self.e=self.a/self.b
        print("division",self.e)
    def sub(self):
        self.f=self.a-self.b
        print("Sub",self.f)


a=int(input("enter 2 number"))
b=int(input())
x=First(a,b)

x.sum()
x.mul()
x.div()
x.sub()