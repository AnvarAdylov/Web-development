import socket

HOST = '127.0.0.1'
PORT = 1991


def handler(conn):
    try:
        data1 = conn.recv(1024).decode().strip()
        num1 = float(data1)
        data2 = conn.recv(1024).decode().strip()
        num2 = float(data2)
        sum_result = num1 + num2
        product_result = num1 * num2
        difference_result = num1 - num2
        try:
            quotient_result = num1 / num2
        except ZeroDivisionError:
            quotient_result = 'Infinity (division by zero)'

        conn.sendall(f"Sum: {sum_result}\n".encode())
        conn.sendall(f"Product: {product_result}\n".encode())
        conn.sendall(f"Difference: {difference_result}\n".encode())
        conn.sendall(f"Quotient: {quotient_result}\n".encode())
    except ValueError:
        err_mes = "Error: Invalid input. Please send valid numbers.\n"
        conn.sendall(err_mes.encode())
    finally:
        conn.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))

s.listen()

print(f'Waiting for connection on {PORT} port')

while True:
    conn, addr = s.accept()
    print(f'Connected by {addr}')
    handler(conn)
