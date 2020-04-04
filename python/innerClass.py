''' inner class '''
class Family :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.address = self.Address() 
    def memberDetails(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        self.address.showAddress() 
    class Address :
        def __init__(self):
            self.street = "Vivekananthar Street"
            self.city = "dubai"
        def showAddress(self):
            print("Street :  ",self.street)
            print("City : ",self.city)
member1 = Family('karthi',23)
member2 = Family('kavi',25)
member1.memberDetails()
member2.memberDetails()

address1 =member1.Address()  # creating object for inner class using outer class
address1.showAddress()


''' OUTPUT
Name :  karthi
Age :  23
Street :   Vivekananthar Street
City :  dubai
Name :  kavi
Age :  25
Street :   Vivekananthar Street
City :  dubai
Street :   Vivekananthar Street
City :  dubai
'''

