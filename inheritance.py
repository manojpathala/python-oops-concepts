class A:
    def feature1(self):
        print("feature 1 is working")
    
#single level inheritance
class B(A):
    def feature2(self):
        print("feature 2 is working")
    
#multi level inheritance
class C(B):
    def feature3(self):
        print("feature 3 is working")
obj=A()
obj.feature1()
#single level inheritance
single=B()
single.feature1()
single.feature2()
#multi level inheritance
multi_level=C()
multi_level.feature1()
multi_level.feature2()
multi_level.feature3()
#mutiple inheritance
class A:
    def feature1(self):
        print("feature 1 is working")
class B:
    def feature2(self):
        print("feature 2 is working")
class C(A,B):
    def feature3(self):
        print("feature 3 is working")
multiple=C()
multiple.feature1()
multiple.feature2()
multiple.feature3()
