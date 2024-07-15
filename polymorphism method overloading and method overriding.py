#using none method overloading is formed
class A:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
            return s
        elif a!=None and b!=None:
            s=a+b
            return s
        else:
            s=a
        return s
p=A(29,33)
print(p.sum(6,8))
print(p.sum(6,3,2))
print(p.sum(2))
#method overriding means it gives the first preference of that class methods in case the current method has nothing to print then it goes to inheritance
#first preferecnce to the current object methods while something in the current object method
class A():
    def show(self):
        print("in A")
class B(A):
    def show(self):
        print("in B")
p1=B()
p1.show()
#going to inheritance when nothing in the current method
class A():
    def show(self):
        print("in A")
class B(A):
    pass
p1=B()
p1.show()
