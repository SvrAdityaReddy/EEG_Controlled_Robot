import socket

HOST = '127.0.0.1'  
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    count=0
    with open("t2.csv") as f: 
        for line in f: 
            count=count+1
            print(line)
            s.send(str.encode(line)), 
    print(count)
            