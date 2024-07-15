#duck typing means created object from a class is used in another class as a object to run the function
class pycharm:
    def execute(self):
        print("compiling")
        print("run")
class laptop:
    def code(self,ide):
        ide.execute()
ide=pycharm()
lap1=laptop()
lap1.code(ide)