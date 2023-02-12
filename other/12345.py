import socket

HOST = "137.151.29.179"  # The server's hostname or IP address
PORT1 = 12345  # The port used by the server
PORT2 = 54321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT1))
    initial = s.recv(4096).decode(encoding="UTF-8")
    print(initial)

    word = initial.split()[-1] + '\n'
    print(word)

    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((HOST, PORT2))
    msg = s2.recv(4096)
    print(msg)

    s2.recv(4096)
    s2.sendall(bytes(word, encoding="UTF-8"))
    res = s2.recv(4096).decode('utf-8')
    print("res", res)
    thing = res[11:] + '\n'
    print(thing)
    
    s.recv(8192)
    s.sendall(bytes(thing, encoding="utf-8"))
    print(s.recv(8192).decode("utf-8"))

