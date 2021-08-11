import socket
import threading #faz com que rode tudo e se empacar um , ele continua no flow

HEADRER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print("[NEW CONNECTION] {} connected.".format(addr))

    connected = True
    while connected:
        msg_length = conn.recv(HEADRER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        
        if msg == DISCONNECT_MSG:
            break

        print("[{}]".format(addr))
        print("[{}]".format(msg))

    conn.close()


 
def start():
    server.listen(5)
    print("[LISTENING] The server is listening on {}".format(SERVER))
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client , args=(conn, addr))
        thread.start()
        print("[ACTIVE CONNECTIONS] {}".format(threading.active_count() - 1))

print("[STARTING] The server is starting...")
start()