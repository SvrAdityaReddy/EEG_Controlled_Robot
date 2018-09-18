import socket

HOST='127.0.0.1'
PORT=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        try:
            while True:
                data = conn.recv(1024)
                if data:
                    print(data.decode())
        except KeyboardInterrupt:
            s.close()
    s.close()