'''  Generator  '''
''' Used for not to store larger amount of data in a varible(reduce stack memory usage) '''
def topten():
   n=1
   while n<=10 :
      sq =n*n
      yield sq                   #Yield Generates Generatorobject       
      n+=1

values = topten()
print(values.__next__())       #gets first yeild
print(topten().__next__())       #gets second yeild

values = topten()
for i in values:                 #calls __next__()       
   print(i)
