import socket
from threading import Thread
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='ngrok_ip'
port=12500
conn.connect((host,port))
print("Connected...")
f=open('a.jpg','wb')
condition=True
while condition:
	image=conn.recv(1024)
	if str(image)=="b''":
		condition=False
	f.write(image)