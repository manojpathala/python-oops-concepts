class computer:
    def __init__(self):
        self.name="Ravi"
        self.age=20
    def update(self):
        self.age=30
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=computer()
c2=computer()
print(c1.age)
c1.update()
print(c1.age)
c2.age=20
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")
