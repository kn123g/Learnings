from array import  *
from math  import *

n=int(input("Enter the size "))
while(n<6 or (n%2)!=0):
    n=int(input("Enter number greater than 6 and even number "))


k=n
for i in range(1,n+1) :
    if (i>int(floor(n/2))) :
        k=k-1;
    for j in range(1,n+2) :
        if (i<2) :
            if j==1 or  j == int(ceil((n+2)/2)) or (j==(n+1)) :
                    print("    ", end ="")
            else :
                print("*   ", end ="")
        if (i>1 and i<3) :
            if j==1 or  j == int(ceil((n+2)/2)) or (j==(n+1)) :
                    print("*   ", end ="")
            else :
                print("    ", end ="")
        if (i>2 and i<int((n/2))+1) :
            if j==1 or (j==(n+1)) :
                    print("*   ", end ="")
            else :
                print("    ", end ="")
        if (i>int(floor(n/2))) :
            #print("i : %i j : %i k : %i" %(i,j,k))
            
            if (j==(n-(k-1))) or (j==(k+1)) :
                    print("*   ", end ="")
            else :
                print("    ", end ="")         
    print("")
    print("")

"""OUTPUT
Enter the size 6
    *   *       *   *       

*           *           *   

*                       *   

    *               *       

        *       *           

            *               
"""
