#create a class usig class keyword
class computer:
    #__init__ is the method used to intialising the variables.Here,Attributes are nothing but variables. 
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is:",self.cpu,self.ram)
#object creation
com1=computer("i5",16)
com2=computer("Ryzen 5",8)
#calling class methods using the object
com1.config()
com2.config()