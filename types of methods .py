class student:
    universtity="Sri Venkateswara University"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def get_university_name(cls):
        return cls.universtity
    @staticmethod
    def info():
        return "This is a static class"
s1=student(33,22,11)
s2=student(22,33,66)
#calling the instance method using instance variables
print(s1.avg())
#calling the class method
print(s1.get_university_name())
#calling the static method
print(s1.info())