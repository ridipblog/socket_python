import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='3.142.167.54'
port=12500
s.connect((host,port))
con=True
while con:
	msg=input("Enter Msg: ")
	s.send(msg.encode("utf-8"))
	if(msg=="quit"):
		con=False
		s.close()
