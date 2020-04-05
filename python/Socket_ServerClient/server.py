from socket import *
s = socket()
s.bind(("localhost", 9999))
s.listen(3)
while True:
    c, address = s.accept()
    print("Connected to ", address)
    c.send(bytes("Server welcomes you", "utf-8"))

    c.close()
