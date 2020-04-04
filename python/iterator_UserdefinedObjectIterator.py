''' Iterator '''
nums = [1,2,3,4,5,6]
fornums = range(1,11)
iterator1 = nums.__iter__()      # calls 'list' class's object method : __iter__()  
iterator2 = nums.__iter__()
print(iterator1.__next__())      # calls 'list' class's object method : __next__()
print(next(iterator1))
print(iterator2.__next__())
print(next(iterator2))
print("Printing using for loop")
for i in fornums:
   print(i)

''' User defined Object iterator '''
print("User defined Object iterator")
class nums:
   def __init__(self,length):
      self.num =0
      self.iterator=0
      self.length = length
   def __iter__(self):
      return self
   def __next__(self):
      
      if self.iterator < self.length:
         self.num +=1
         self.iterator +=1
         return self.num
      else:
         raise StopIteration
         

list1 = nums(20)

for i in list1 :                 # calls 'nums' class's object methods : __iter__(),__next__() 
   print(i)
