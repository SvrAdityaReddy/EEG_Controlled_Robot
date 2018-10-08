import socket

HOST='10.10.10.10'
PORT=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    count=0
    mean=0
    j=0
    with conn:
        print('Connected by', addr)
        try:
            while True:
                data = conn.recv(1024)
                if data:
                    dat=data.decode()
                    dat=dat.splitlines()
                    for i in range(len(dat)):
                        if(count!=8):
                            mean=mean+abs(float(dat[i]))
                            count=count+1
                        if(count==8):
                            val=abs(float(dat[i]))
                            mean=mean/8.0
                            if(abs(val-mean)>100):
                                j=j+1
                                print("Blink",j)
                            count=0
                            mean=0
        except KeyboardInterrupt:
            s.close()
    s.close()