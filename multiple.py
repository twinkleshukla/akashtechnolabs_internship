class MyParentClass1():
    def method_Parent1(self):
        print("parent1 method called")
class MyParentClass2():
    def method_Parent2(self):
        print("parent2 method called")
class ChildClass(MyParentClass1,MyParentClass2):
    def child_method(self):
        print("child method")

c=ChildClass()
c.method_Parent1()
c.method_Parent2()
c.child_method
