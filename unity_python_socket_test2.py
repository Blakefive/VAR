import socket

HOST = '192.168.0.8' 
PORT = 8001   

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()

client_socket, addr = server_socket.accept()

print('Connected by', addr)

k = 0

while True:
    msg = client_socket.recv(4507)
    print(msg.decode())
    k += 1
    

client_socket.close()
server_socket.close()
