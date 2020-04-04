''' Polymorphism '''
''' Duck Typing '''
class Eclipse:
   def execute(self):
       print("Eclipse IDE")
class Intelligence:
    def execute(self):
        print("Intelligence IDE")

class Laptop:
    def run(self,ide):
        ide.execute()
lap = Laptop()
ide=Eclipse()
lap.run(ide)
ide =Intelligence()
lap.run(ide)

''' Operator Overloading '''

class SumObject:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        a=self.a+other.a            #a is a temporary variable
        b=self.b+other.b            #a is a temporary variable
        result = SumObject(a,b)
        return result
    def __sub__(self,other):
        a=self.a-other.a            #a is a temporary variable
        b=self.b-other.b            #a is a temporary variable
        result = SumObject(a,b)
        return result
obj1 = SumObject(2,3)
obj2 = SumObject(4,5)
sumObject = obj1 + obj2            #SumObject.__add__(obj1,obj2)
subObject = obj1 - obj2  
print("Sum of two object :",sumObject.a,sumObject.b)
print("Sub of two object :",subObject.a,subObject.b)

''' OUTPUT
Eclipse IDE
Intelligence IDE
Sum of two object : 6 8
Sub of two object : -2 -2
'''



