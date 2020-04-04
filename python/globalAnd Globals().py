''' changing global variable '''
a=10
def globalValueChange():
    global a
    a=11
    print("global value change from 10 to 11 (inside scope) : ",a)
globalValueChange()
print("global value print (outside scope) : ",a)


''' changing global variable and using same local variable '''
c=20
def globalsValueChange():
    globals()['c']=21
    c=30
    print("global value change from 20 to 21  and printing (inside scope) : ",c)
globalsValueChange()
print("global value print (outside scope) : ",c)
