''' Multi Threading  '''
''' Each Thread may run in separate core '''
from threading import *
from time import *
class odd (Thread):                       #Inherited Thread Class
   def __init__(self,length):
      super().__init__()                  #Calls Thread class __init__()
      self.length = length
   def run(self):                         #only one argumentn allowed
      for i in range(1,self.length):
         sleep(1)
         if(i%2!=0):
            print(i)
class even (Thread):                      #Inherited Thread Class
   def __init__(self,length):
      super().__init__()                  #Calls Thread class __init__()
      self.length = length
   def run(self):                         #only one argumentn allowed
      for i in range(1,self.length):
         sleep(1)                   
         if(i%2==0):
            print(i)

odd = odd(10)
even = even(10)

odd.start()                               #calls run()
sleep(0.01)                               #main Thread sleeps for 0.01 secs
even.start()                              #calls run()

odd.join()
even.join()
print("bye")





