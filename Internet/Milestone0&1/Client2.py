import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.102"
localhost = "127.0.0.1"
port = 55410
client_socket.connect((localhost, port))

while True:
    message = input("Message:")
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response:{response}")
    if response == "Goodbye":
        break

client_socket.close()