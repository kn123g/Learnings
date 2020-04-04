''' Linear Search '''
nums = list(range(1,11))
find = int(input("enter num to find "))

for i in range(0,len(nums)):
   if nums[i] == find:
      print(find, "in index : ",i)
      break
else:
   print("number not found")

''' Binary Search '''
start = 0
end = len(nums) - 1

found = False
while start < end :                                         # main logic to stop loop when given number is not found till end of list
   print("Start and End : ",start,end)
   mid = (start + end)//2                                   # main logic to find mid eachtime     
   if nums[mid] == find :
      print("found in index : ",mid)
      break
   elif nums[mid] < find :
      start = mid + 1
   elif nums[mid] > find :
      end = mid  - 1
else :
   print("Not found")

# Selection sort  uses less cpu power and memory than bubble sort (both already know)

