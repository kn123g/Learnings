''' Types of methods
Class Method, Object Method, Static Method '''

class Methods :
    welcome = "Hai"
    def __init__(self):
        self.a=2
        self.b=3
    def objectMethod(self):
        return self.a+self.b
    def classMethod(cls):
        return cls.welcome
    def staticMethod():
        return "bye"
obj = Methods()
print(obj.objectMethod())
print(Methods.classMethod(Methods))
print(Methods.staticMethod())

''' OR  '''

class Methods1 :
    welcome = "Hai"
    def __init__(self):
        self.a=2
        self.b=3
    def objectMethod(self):
        return self.a+self.b
    @classmethod                            #change1
    def classMethod(cls):
        return cls.welcome
    @staticmethod                            #change2
    def staticMethod():
        return "bye"
obj = Methods1()
print(obj.objectMethod())
print(Methods1.classMethod())                           #change3
print(Methods1.staticMethod())

''' OUTPUT
5
Hai
bye
5
Hai
bye
'''


        
