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
	print("")
	command=input("Enter Command ")
	if(command=="create file"):
		conn.send(command.encode())
		print("Send..")
	elif(command=="dir"):
		conn.send(command.encode())
		print("Send..")
		folder=conn.recv(1024)
		folder=folder.decode()
		print("Current Folder "+folder)
	elif(command=="quit"):
		conn.send(command.encode())
	elif(command=="allfiles"):
		conn.send(command.encode())
		print("Send..")
		user=input("Enter Path ")
		conn.send(user.encode())
		all_files=conn.recv(5000)
		all_files=all_files.decode()
		print("Files "+all_files)