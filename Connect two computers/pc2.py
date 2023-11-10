import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.1.190'  
server_port = 12345  

client_socket.connect((server_ip, server_port))
print(f"Connected to {server_ip}:{server_port}")

message = "Pc2 working"
client_socket.send(message.encode('utf-8'))

response = client_socket.recv(1024).decode('utf-8')
print(f"Server response: {response}")

client_socket.close()
