'''**
 * @author S.V.R. Aditya Reddy
 * @email Aditya.seelapureddy@tutanota.com
 * @create date 2018-10-18 20:57:36
 * @modify date 2018-10-18 20:58:01
 * @desc [description]
*'''

import sys
import os
import time
import socket
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

HOST = '10.10.10.10'  
PORT = 65432

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
with open(sys.argv[2]) as f: 
    for line in f: 
        s.send(str.encode(line)), 
f.close()

class my_handler(FileSystemEventHandler):
    def on_modified(self,event):
        # data=subprocess.check_output(['tail', '-1', sys.argv[2], '|', 'cut', '-d ","', '-f2'])
        os.system('tail -1 '+ sys.argv[2] + ' | cut -d "," -f2 > tmp')
        data=open('tmp', 'r').read()
        print(data)
        global s
        s.send(str.encode(data))

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
s.close()
