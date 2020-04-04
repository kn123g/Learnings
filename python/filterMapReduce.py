from functools import *
'''filter normal usage  '''
def is_even(temp):
    return temp%2==0
filterResult = list(filter(is_even, [1,2,3,4,5,6,7,8,9,10]))

print("even numbers using def function (filter) : ",filterResult)


print("odd numbers using lambda function (filter) : ",list(filter(lambda temp : temp%2 != 0 ,[1,2,3,4,5,6,7,8,9,10])))

'''Map normal usage  '''
def double(temp):
    return 2*temp
mapResult = list(map(double,filterResult))
print("double even filter list using def function (Map) : ",mapResult)
print("double even filter list using lambda function  (Map) : ",list(map(lambda temp : 2*temp,filterResult)))

'''Reduce normal usage  '''
def sumList(a,b):
    return a+b
ReduceResult = reduce(sumList,mapResult)
print("Sum Map list using def function (Map) : ",ReduceResult)
print("Sum Map list using lambda function  (Map) : ",reduce(lambda a,b : a+b,mapResult))
