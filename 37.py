class First:
    def first(self):
        print("first")
class Second(First):
    def second(self):
        print("Seconmd ")
class Third:
    def third(self):
        print("third")
class Fourth(Second,Third):
    def fourth(self):
        print("forth")

x=Fourth()
x.first()
x.second()
x.third()
x.fourth()