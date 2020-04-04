import math

n=int(input('enter thenumber to check'))

"""" method 1 """
for i in range(2,n):
     if(n%i) == 0:
          print("not prime number")
          break
else:
     print("prime number")

"""" method 2 """
for i in range(2,(math.floor(math.sqrt(n)))+1):
     if(n%i) == 0:
          print("not prime number")
          break
else:
     print("prime number")
