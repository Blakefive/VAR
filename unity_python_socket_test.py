import socket

HOST = '192.168.0.8' 
PORT = 8000       

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()

client_socket, addr = server_socket.accept()

print('Connected by', addr)

k = 0

while True:
    
    msg = "mpu6050 " + str(k)
    client_socket.sendall(msg.encode())
    print('send 완료 '+ str(k) )
    k += 1
    

client_socket.close()
server_socket.close()
