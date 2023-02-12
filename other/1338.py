import socket

HOST = "137.151.29.179"  # The server's hostname or IP address
PORT = 1338  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(100):
        initial = s.recv(4096)
        thing = s.recv(8192)
        print(initial)
        print(thing)
        thing = thing.decode("utf-8").lstrip('\n')
        print(thing)
        s.sendall(bytes(thing, encoding="utf-8"))
    s.close()
