import socket
import threading #faz com que rode tudo e se empacar um , ele continua no flow

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    pass
 
def start():
    pass

