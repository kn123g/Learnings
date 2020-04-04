''' Abstract Class '''
# class having abstract method are abstract class.Abstract class is used to have certain method must be present in child class
from abc import ABC, abstractmethod
class Laptop(ABC) :                 # inherited ABC Abstract base class                          
   @abstractmethod                  # abstractmethod decorator (making method abstract)
   def process(self):
      pass

class Eclipse(Laptop) :
   def process(self):
      print("Running Eclipse")

class Intelligence(Laptop):
   def process(self):
      print("Running Intelligence")

class Programmer:
   def execute(self,tool):
      tool.process()

obj = Programmer()
tool1 = Eclipse()
tool2 = Intelligence()
obj.execute(tool1)


