class MyParentClass():
    def func1(self):
        print("parent method called")
class ChildClass(MyParentClass):
    def func1(self):
        print("child method called")
c=ChildClass()
c.func1()