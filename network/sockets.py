__author__ = 'alexandre'
import socket


print("creating socket")
s = socket.socket()
print("done")

port = socket.getservbyname('http', 'tcp')

s.connect(("www.uol.com", port))

print("Connected from: ",  s.getsockname())
print("Connected to: ", s.getpeername())

