''' File Handling  '''
''' ReadFile '''
readtxt = open("D:\Learning\python\Files\FileRead.txt",'r')
readtxt1 = open("D:\Learning\python\Files\FileRead.txt",'r')
print ("Print whole file " ,readtxt.read())

print ()
print ("Printing using readline iterator ")

print (readtxt1.readline(),end='')
print (readtxt1.readline(),end='')

print ()
print ("Prints 4 characters from current cursor :",readtxt1.readlines(4))

readtxt.close()
readtxt1.close()

'''' Write File '''
print ()
print ("Write File")
writetxt = open("D:\Learning\python\Files\FileWrite.txt",'w')
writetxt.write("I'm python.\nI was both compiled and interprated, Source code to byte code(compiled), bytecode to Machine code(Interpretor) ")
writetxt.close()

readtxt = open("D:\Learning\python\Files\FileWrite.txt",'r')
print (readtxt.read(),end='')
readtxt.close()

'''' Append File '''
writetxt = open("D:\Learning\python\Files\FileWrite.txt",'a')
writetxt.write("This is all about me")
writetxt.close()

readtxt = open("D:\Learning\python\Files\FileWrite.txt",'r')
print (readtxt.read())
readtxt.close()


''' Reading Image '''
readimage = open("D:\Learning\python\Files\image.jpg",'rb')
print(readimage.read())                                     # print binary of image


''' Write Image '''
writeimage = open("D:\Learning\python\Files\image1.jpg",'wb')
#writeimage.write(readimage.read())
#for i in readimage :
   #writeimage.write(i)
readimage.close()
writeimage.close()



