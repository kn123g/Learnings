''' Class and Object '''
class  Design :
    welcome = 'Hai'                            # welcome Class variable (Static variable) , a,b Instance variable 
    def __init__(self,a,b):                     
        print("Executing Constructor")
        self.a=a
        self.b=b
    
    def startMethod(self):
        print("Executing Methods Printing Sum : ",self.a + self.b,Design.welcome)
        
obj = Design(2,3)
print("Calling in way 1 : ",Design.startMethod(obj))
print("Calling in way 2 : ",obj.startMethod())


print(Design.welcome)
print(obj.welcome)

Design.welcome = 'bye'

print(Design.welcome)
print(obj.welcome)

obj.welcome = "i'm back"     #Cannot change Class variable using object

print(Design.welcome)
print(obj.welcome)


''' Output
Executing Constructor
Executing Methods Printing Sum :  5 Hai
Calling in way 1 :  None
Executing Methods Printing Sum :  5 Hai
Calling in way 2 :  None
Hai
Hai
bye
bye
bye
i'm back '''
