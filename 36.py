class School:
    def school(self):
        print("hello world")
class Student1(School):
    def std1(self):
        print("anju")
class Student2(School):
    def std2(self):
        print("ammu")
class Student3(Student1,School):
    def std3(self):
        print("anjana")
x=Student3()
x.std1()
x.std3()