class Frst:
    def frst(self):
        print("heloo world")
class Second(Frst):
    def second(self):
        print("Apple")
class Third(Second):
    def third(self):
        print("orange")

x=Third()
x.frst()
x.second()
x.third()