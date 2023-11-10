import socket
import threading

host = '192.168.1.190'
port = 55555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

username = input("Enter Username: ")
client_socket.send(username.encode('utf-8'))
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode('utf-8'))
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
while True:
    message = input()
    client_socket.send(message.encode('utf-8'))
