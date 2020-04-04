def functionnDefaultArgument(welcome,name='karthi'):
     return welcome+name
def function(welcome,name):
     return welcome+name
def functionArgOrder(a,b):
     return a,b
def functionTuplesType(*a):
     return type(a)
def functionTuples(*a):
     return a[0]
def functionReturnTwoValues(a,b):
     return a+b,a-b
def functionKeywordVaribleLenthArg(a,**b):
     print(type(b))
     print(a)
     for i,j in b.items():
          print(i,j)
     print ("Type of b.items() : " ,type(b.items()))
     print (" Dict_items print (b.items()) : " ,b.items())
     return a,b
''' Lambda function '''
lamfunc = lambda welcome,name='karthi' : welcome+name
print("Normal function : ",function('hai','kavi'))
print("Defaul Argument function : ",functionnDefaultArgument('hai'))
print("Change Order of Argument function b=3,a=8: ",functionArgOrder(b=3,a=8))
print("Tuple Argument function : ",functionTuplesType('hai'))
print("Tuple Argument function : ",functionTuples("hai","bye"))
print("Function return Two values : ",type(functionReturnTwoValues(2,4)))
c,d=functionReturnTwoValues(2,4)
print("Function return Two values : ", functionReturnTwoValues(2,4) , " assigned to variable c and d  : ",c,"   ",d)
print("Function Keyword Varible Lenth Argument : " )
functionKeywordVaribleLenthArg(2,name="karthi",age=23,dept="IT")
print("Lambda Function with default argument : " , lamfunc('hai'))


