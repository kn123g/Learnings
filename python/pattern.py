""" method 1 """
n = int(input('enter the n : '))

for i in range(0,n//2):
     #print ('hai'  ,i)
     even = 0
     for j in range((n//2)-1,i,-1):
         print(" ",end="")
     for j in range(0,i):
         even+=1
         if(even%2 == 0):
             print(" ",end="")
         else:
             print("*",end="")
         
     for j in range(1,i):
         even+=1
         if(even%2 == 0):
             print(" ",end="")
         else:
             print("*",end="")
         
     print("")



for i in range(2,n//2):
     #print ('hai'  ,i)
     even = 0
     for j in range(1,i):
         print(" ",end="")
     for j in range((n//2)-1,i,-1):
         even+=1
         if(even%2 == 0):
             print(" ",end="")
         else:
             print("*",end="")
     for j in range(n//2,i,-1):
         even+=1
         if(even%2 == 0):
             print(" ",end="")
         else:
             print("*",end="")
     print("")

"""
    
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
"""



""" method 2 """
for i in range(0,n//2): 
    for j in range(i+1,n//2):
        print(" ",end="")
    for k in range(-1,i):
        print("* ",end="")
    for l in range(0,i):
       # print("*",end="")
       pass
    print("")

for i in range(1,n//2): 
    for j in range(0,i):
        print(" ",end="")
    for k in range(i,n//2):
        print("* ",end="")
    for l in range(i+1,n//2):
      #  print("*",end="")
      pass
    print("")
         
     
        
