''' Method Overloading '''
''' Method overloading is not support in python but we can use trick and make it happen '''
class MethodOverloading:
    def sum(self,a=None,b=None,c=None):
        if a==None and b==None and c ==None :
            return 0
        elif b==None and c==None:
            return  a
        elif c==None:
            return a+b
        else:
            return a+b+c
obj = MethodOverloading()
print("Method Overloading obj.sum(1,2)",obj.sum(1,2))
print("Method Overloading obj.sum(1,2,3)",obj.sum(1,2,3))
print("Method Overloading obj.sum(1)",obj.sum(1))
print("Method Overloading obj.sum()",obj.sum())


class A:
    def show(self):
        print("hai")
class B(A):
    def show(self):
        print("overriding hai")
obj = B()
obj.show()

''' Output:
Method Overloading obj.sum(1,2) 3
Method Overloading obj.sum(1,2,3) 6
Method Overloading obj.sum(1) 1
Method Overloading obj.sum() 0
overriding hai '''
