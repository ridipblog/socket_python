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
class send(Thread):
	def run(self):
		while True:
			msg=input("\nEnter Msg: ")
			conn.send(msg.encode())
			print("Sent...")
class receive(Thread):
	def run(self):
		while True:
			get_m=conn.recv(1024)
			print("\nRececie : "+get_m.decode())
t1=send()
t2=receive()
t1.start()
t2.start()