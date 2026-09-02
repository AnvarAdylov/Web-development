import socket
import math

HOST = '127.0.0.1'
PORT = 2345


def factorial(n):
    if n > 50000:
        return "Error: Number is too large"
    else:
        return str(math.factorial(n))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))

s.listen()

print(f'Waiting for connection on {PORT} port')

while True:
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        data = conn.recv(1024)
        if not data:
            break
        try:
            number = int(data.decode().strip())
            response = factorial(number)
        except ValueError:
            response = "Error: Invalid input, please enter a valid integer"
        conn.sendall(response.encode())
        print(f'Sent response: {response}')

conn.close()

s.close()
