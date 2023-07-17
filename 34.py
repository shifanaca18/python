class Calculation:
    def data(self):
        self.a=int(input("Enter PA"))
        self.b=int(input("Enter RI"))
        self.c=int(input("Enter NY"))
    def intrest(self):
        self.d=self.a*self.b/100
        print("intrest",self.d)
    def balance(self):
        self.h=self.d + self.a
        print("Bank balance is ",self.h)
    def emi(self):
        self.i=self.a+(self.d+self.c)
        self.m=self.i/(self.c*12)
        print("Emi",self.m)
emi=Calculation()
emi.data()
emi.intrest()
emi.balance()
emi.emi()

