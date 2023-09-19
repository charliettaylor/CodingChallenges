import socket

vault: dict[str, str] = {"version": "charlie db"}


def insert(data: str) -> None:
    key, value = data.split("=", 1)
    if key != "version":
        vault[key] = value


def retrieve(data: str) -> str:
    if data in vault:
        return vault[data]
    else:
        return ""


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", 8888))
print("Server listening on port 8888")

while True:
    data, address = server_socket.recvfrom(999)

    if data is None:
        continue

    msg = data.decode()
    print("req", msg)

    if "=" in msg:
        insert(msg)
    else:
        server_socket.sendto(f"{msg}={retrieve(msg)}".encode(), address)
        print("res", f"{msg}={retrieve(msg)}")
