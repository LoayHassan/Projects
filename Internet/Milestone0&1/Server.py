import socket
import threading


host = "192.168.1.102"
localhost = "127.0.0.1"
port = 55410
clientlock = threading.Lock()

def threadding(client_socket, client_address):

    print(f"Accepted connection from {client_address}")
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received from client:{message}")
        if message.upper() == "END":
            print(f"Connection is closed for:{client_address}")
            response = "Goodbye"
            client_socket.send(response.encode('utf-8'))

            break
        response = message.upper()
        client_socket.send(response.encode('utf-8'))


def main():
    print("Server listening for connections...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((localhost, port))
    server_socket.listen(5)
    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=threadding, args=(client_socket, client_address))
        client_handler.start()
if __name__ == '__main__':
    main()