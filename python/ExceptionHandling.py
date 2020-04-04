'''  Exception Handling  '''
''' checked exception are compile time errors
unchecked exception are runtime errors '''
a=10
try:
   b= int(input("Enter number"))
   a=a/b
     
except ArithmeticError as a:
   print(a)
except ValueError as a:
   print(a)
except Exception as w:
   print(w)
finally:
   print("bye")
