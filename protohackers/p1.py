import socket
import json
import threading
from functools import lru_cache


def is_prime(n) -> bool:
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def send_response(s: socket.socket, payload: dict) -> None:
    '''helper'''
    response = json.dumps(payload)
    s.send(bytes(response + "\n", "utf-8"))


def handle_client(client: socket.socket) -> None:
    """Function to handle client connections"""
    while True:
        data = client.recv(8192 * 8192)
        if not data:
            break

        lines = list(filter(lambda x: len(x) > 0 or x.isspace(), data.decode().split('\n')))
        print(lines)
        for payload in lines:
            try:
                j = json.loads(payload)
            except json.JSONDecodeError:
                res = {"method": "isPrime\n", "prime": False}
                print("json", payload)
                send_response(client, res)
                continue

            res = {"method": "isPrime", "prime": False}
                
            try:
                if not (isinstance(j["number"], int) or isinstance(j["number"], float)) or isinstance(j["number"], bool):
                    print(j["number"], type(j["number"]))
                    raise TypeError
                num: int = int(j["number"])
                method: str = str(j["method"])
            except:
                res["method"] = "\n"
                send_response(client, res)
                continue

            if method != "isPrime":
                print("malo", num, res)
                res["method"] = "\n"
                send_response(client, res)
                continue

            if not is_prime(int(num)):
                send_response(client, res)
                continue

            res["prime"] = True
            print("succ", res)
            send_response(client, res)

    client.close()


PORT = 8888
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(5)
print(f"Server listening on port {PORT}")

while True:
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")

    # Create a thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
