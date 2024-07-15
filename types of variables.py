class car:
    #class variabel or static variable which are out side of the init method and inside of the class 
    wheels=3
    def __init__(self):
        #instance variables which are inside the constructor or init method
        self.mil=20
        self.company="Benz"
c1=car()
c2=car()
#printing the instance class variables
print(c1.mil,c2.company)
print(c2.mil,c2.company)
#printing the class variable or static variables and also with some of instance variables
print(c1.mil,c1.company,c1.wheels)
print(c2.mil,c2.company,c2.wheels)
