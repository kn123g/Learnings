''' Normal Programs '''
''''fibanacci series '''
def fibanacciSeries(n) :
    a,b=0,1
    print(a)
    print(b)
    for i in range(n-2) :
        a,b=b,a+b
        print(b)
     
fibanacciSeries(int(input("enter the length : ")))
#fibanacciSeries(n=int(input("enter the length : "))  n= also used

''' Factorial of number using recursion '''
n= int(input("Enter a number to find factorial "))
def fact(n) :
    if(n>1):
        return fact(n-1) * n
    else :
        return 1

print("Factorial of given number is : ",fact(n))
