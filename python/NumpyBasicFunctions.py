from numpy import *
normalarr = array([2,5,8.0])
arr = array([2,3,4.0,5,2],int)
normalarr = normalarr*5
newarray = copy(normalarr)
concatenatearray = concatenate([arr,newarray])
arangearray = arange(1,10,1)
linespacearray = linspace(1,10,2)
logspacearray= logspace(2,10,5)
zerosarray=zeros(5,int);
onesarray=ones(5,int);
squarerootarray = sqrt(normalarr)
sumarray=sum(arr)
minarray=min(arr)
maxarray=max(arr)
uniquearray=unique(arr)
print("normal array       ",normalarr,"        Address ID" ,id(normalarr),end="\n")
print("with array type    ", arr,"        Address ID" ,id(arr))
print("copied array       ", newarray,"        Address ID" ,id(newarray))
print("concatenate array       ", concatenatearray,"        Address ID" ,id(concatenatearray))
print("arange array       ", arangearray,"        Address ID" ,id(arangearray))
print("linspace array     ", linespacearray,"        Address ID" ,id(linespacearray))
print("logspace array     ", logspacearray,"        Address ID" ,id(logspacearray))
print("zeros array   ", zerosarray,"        Address ID" ,id(zerosarray))
print("ones array    ", onesarray,"        Address ID" ,id(onesarray))
print("sum array    ", sumarray,"        Address ID" ,id(sumarray))
print("min array    ", minarray,"        Address ID" ,id(minarray))
print("max array    ", maxarray,"        Address ID" ,id(maxarray))
print("unique element in array    ", uniquearray,"        Address ID" ,id(uniquearray))





