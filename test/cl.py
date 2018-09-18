import socket

HOST = '127.0.0.1'  
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open("t.csv") as f: 
        for line in f: 
            s.send(str.encode(line)), 
            