import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.190' 

port = 12345  
server_socket.bind((host, port))
server_socket.listen()
print(f"Server listening on {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

data = client_socket.recv(1024).decode('utf-8')
print(f"Received data: {data}")

response = "PC1 Working"
client_socket.send(response.encode('utf-8'))

client_socket.close()
server_socket.close()
