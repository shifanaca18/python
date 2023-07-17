class Calculation:
    def sum(self,a,b):
        return a+b;
class Calculation2:
    def multy(self,a,b):
        return a*b;
class Divider(Calculation,Calculation2):
    def div(sef,a,b):
        return a/b;

d=Divider()
print(d.sum(100,200))
print(d.multy(100,200))
print(d.div(100,200))
