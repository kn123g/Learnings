from socket import *
c = socket()
c.connect(("localhost", 9999))
print(c.recv(1024).decode())