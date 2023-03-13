import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='ngrok_ip'
# command for cmd -> tcp http 4045
# command for cmd -> ping tcp generate link
port=12500
s.connect((host,port))
con=True
while con:
	msg=input("Enter Msg: ")
	s.send(msg.encode("utf-8"))
	if(msg=="quit"):
		con=False
		s.close()
