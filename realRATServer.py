# import socket
# import os
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # host=socket.gethostbyname(socket.gethostname())
# host='127.0.0.1'
# port=4045
# s.bind((host,port))
# s.listen(2)
# socketclient,address=s.accept()
# print("Connection From "+str(address))
# con=True
# while con:
# 	msg=input("\nEnter Command ")
# 	socketclient.send(msg.encode())
# 	if(msg=="quit"):
# 		con=False
# 		s.close()



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
			if(msg=="quit"):
				s.close()
			
t1=send()
t1.start()