import socket
from threading import Thread
import os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=4045
s.bind((host,port))
s.listen(5)
conn,add=s.accept()
print("Connection From "+str(add))
while 1:
	data=conn.recv(1024)
	data=data.decode()
	print(data)