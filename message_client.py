import socket
from threading import Thread
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='3.142.129.56'
port=12500
conn.connect((host,port))
print("Connected...")
class send(Thread):
	def run(self):
		while True:
			msg=input("\nEnter Msg: ")
			conn.send(msg.encode())
			print("\nSent...")
class receive(Thread):
	def run(self):
		while True:
			get_m=conn.recv(1024)
			print("\nRececie : "+get_m.decode())
			if(get_m.decode()=="quit"):
				with open("t.txt","w")as file:
					file.write("Hello")
t1=send()
t2=receive()
t1.start()
t2.start()