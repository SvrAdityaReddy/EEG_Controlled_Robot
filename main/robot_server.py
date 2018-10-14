import socket
import easygopigo3

HOST='10.10.10.10'
PORT=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    count=0
    mean=0
    i=0
    j=0
    rbt = easygopigo3.EasyGoPiGo3()
    m_st=True
    with conn:
        print('Connected by', addr)
        try:
            while True:
                data = conn.recv(1024)
                if data:
                    i=i+1
                    print(i,data)
                    if(i>500):
                        print("data")
                        dat=data.decode()
                        dat=dat.splitlines()
                        # print(data.decode())
                        # print(len(dat))
                        for k in range(len(dat)):
                            # print(float(dat[i]),count)
                            if(count!=8):
                                if(len(dat[k])>=4):
                                    mean=mean+abs(float(dat[k]))
                                    count=count+1
                            if(count==8):
                                if(len(dat[k])>=4):
                                    val=abs(float(dat[k]))
                                    mean=mean/8.0
                                    if(abs(val-mean)>100):
                                        j=j+1
                                        print("Blink",j)
                                        if(m_st):
                                            rbt.backward()
                                            m_st=False
                                        else:
                                            rbt.stop()
                                            m_st=True
                                    count=0
                                    mean=0
        except KeyboardInterrupt:
            s.close()
    s.close()