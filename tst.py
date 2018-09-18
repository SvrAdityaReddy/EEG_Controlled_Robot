import sys
import time
import socket
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

HOST = '127.0.0.1'  
PORT = 65432

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
with open("t.csv") as f: 
    for line in f: 
        s.send(str.encode(line)), 
f.close()

class my_handler(FileSystemEventHandler):
    def on_modified(self,event):
        data=subprocess.check_output(['tail', '-1', "t.csv"])
        # print(data)
        global s
        s.send(data)

path = sys.argv[1] if len(sys.argv) > 1 else '.'
event_handler = my_handler()
observer = Observer()
observer.schedule(event_handler, path, recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    s.close()
    observer.stop()
observer.join()