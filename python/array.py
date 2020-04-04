from array import  *

arr = array('i',[])
n=int(input("Enter size of array : "))
for i in range (n):
    print("Enter " ,i+1 ," Element")
    arr.append(int(input()))
    
arr[0]=1
print(arr)

newarry=array(arr.typecode,arr)
print(newarry)

arr.reverse()
print (arr)
print (newarry)

i=0
while i<len(arr):
    print(arr[i])
    i+=1


print("index of 8 is " ,arr.index(8) +1)
