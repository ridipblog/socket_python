import socket
from threading import Thread
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='3.17.7.232'
port=12476
conn.connect((host,port))
print("Connected...")
image=open('D:\\Gp\\assets\\img\\ridip.jpg','rb')
for i in image:
	conn.send(i)