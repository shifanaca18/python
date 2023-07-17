
class Data:
      def data(self):
        self.a=int(input("Enter 2 anumber"))
        self.b=int(input())
class Sum(Data):
    def sum(self):
        c=self.a+self.b
        print("sum",c)
class Sub(Sum):
      def sub(self):
           d=self.a-self.b
           print(d)
class Multy(Sub):
     def multy(self):
          e=self.a*self.b
          print(e)          
# class Div:
#      def div(self):
#           f=a/b
#           print(f)  
b=Sum()
b.data()
b.sum()
b.sub()
b.multy()
