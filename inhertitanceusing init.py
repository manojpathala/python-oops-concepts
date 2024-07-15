class A:
    def __init__(self):
        print("init A")
    def feature1(self):
        print("feature 1-A is working")
    
#single level inheritance
class B(A):
    def __init__(self):
        #calling super class A in it super() method is used
        super().__init__()
        print("init B")
    def feature2(self):
        print("feature 2 is working")
    
#multi level inheritance
class C(B):
    def __init__(self):
        #calling super class A in it super() method is used
        super().__init__()
        print("init C")
    def feature3(self):
        print("feature 3 is working")
a1=A()
print(a1)
b1=B()
print(b1)
c1=C()
print(c1)
#mutiple inheritance
class A:
    def __init__(self):
        print("init A")
    def feature1(self):
        print("feature 1 is working")
class B:
    def __init__(self):
        super.__init__()
        print("init B")
    def feature2(self):
        print("feature 2 is working")
class C(A,B):
    #in this case method resolution order is applied (MRO) from left to right in the left the class A is present
    def __init__(self):
        super().__init__()
        print("init C")
    def feature3(self):
        print("feature 3 is working")
c1=C()
print(c1)