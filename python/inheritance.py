''' Inheritance '''
''' Single Inheritance '''
class Bird :
    def fly(self):
        print("flying")
class Crow(Bird):
    pass
obj = Crow()
obj.fly()

''' Multiple Inheritance '''
class SkyBird :
    def fly(self):
        print("sky flying")
class LandBird :
    def fly(self):
        print("land flying")
class Chicken(LandBird,SkyBird):
    pass
obj = Chicken()
obj.fly()

''' Multilevel Inheritance '''
class NonHuman_ :
    def fly(self):
        print("NonHuman flying")
class Bird_(NonHuman_) :
    def fly(self):
        print("Bird flying")
class Chicken_(Bird_):
    pass

print("Single Inheritance")

obj = Crow()
obj.fly()

print("Multiple Inheritance")

obj = Chicken()
obj.fly()

print("Multilevel Inheritance")

obj = Chicken_()
obj.fly()


''' OUTPUT
flying
land flying
Single Inheritance
flying
Multiple Inheritance
land flying
Multilevel Inheritance
Bird flying
'''
