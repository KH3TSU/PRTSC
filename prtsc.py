import threading
from queue import Queue
import time
import socket
from plyer import notification
import pyfiglet
from colorama import Fore
print_lock = threading.Lock()
result = pyfiglet.figlet_format("PRTSC")
print(Fore.RED + result)
print("about us ")
print("github KH3TSU : https://github.com/KH3TSU ")
print("github unknoun12 : https://github.com/unknoun12")  
target = input("Enter target: ")

ip = socket.gethostbyname(target)
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print(Fore.GREEN + 'Port',port,": Open")
        con.close()
    except:
        pass



def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()
for x in range(30):
     t = threading.Thread(target=threader)
     t.daemon = True
     t.start()


start = time.time()

# Ports 1-1000
for worker in range(1,1000):
    q.put(worker)

q.join()
