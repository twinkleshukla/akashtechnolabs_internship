class Parent:
    def __init__(self):
        print("calling parent constructor")
    def parentMethod(self):
        print("calling parent method")
class Child(Parent):
    def __init__(self):
        print("calling child constructor")
    def childMethod(self):
        print("calling child method")

        # multilevel inheritance
class SubChild(Child):
    def __init__(self):
        print("calling sub child constructor")
    def subchildMethod(self):
        print("calling sub child method")



sc=SubChild()
sc.subchildMethod()
sc.childMethod()
sc.parentMethod()