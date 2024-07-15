class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.cpu="intel i7"
            self.ram=8
        def show(self):
            print(self.cpu,self.ram)
#creation of outer class object
s1=student("Honda",60)
#creation of inner class object
lap1=student.laptop()
#calling the methods of outer class and inner class
s1.show()
#calling the methods of inner class
lap1.show()