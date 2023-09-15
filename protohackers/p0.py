import socket
import json
import threading


# Function to handle client connections
def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(4096)
        if not data:
            break

        client_socket.send(data)

    # Close the client socket
    client_socket.close()


# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(("0.0.0.0", 8888))

# Start listening for incoming connections
server_socket.listen(5)
print("Server listening on port 8888")

while True:
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")

    # Create a thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
