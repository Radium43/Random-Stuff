import socket
import threading

host = '192.168.1.190'
port = 55555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
print(f"Server is listening on {host}:{port}")
clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break

            broadcast(message, client_socket)

        except:
            clients.remove(client_socket)
            break

while True:
    client_socket, client_address = server_socket.accept()

    clients.append(client_socket)

    print(f"Connection from {client_address} established.")

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
