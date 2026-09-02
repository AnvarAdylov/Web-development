import socket
import random

HOST = '127.0.0.1'

PORT = 1234
quotes = [
    "vini vidi vici",
    "ooo ooo oooo - Gwimbly the iconic videogame character",
    "yo - random dude on internet",
    "hastalavista i will be back - Terminator",
    "i am your grandpa - my grandpa",
    "Imagine its what you wanted and see how it makes you feel",
    "Life is what happens when you're busy making other plans. - John Lennon"
]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))

s.listen()

print(f'Waiting for connection on {PORT} port')

conn, addr = s.accept()

print(f'Connected by {addr}')

quote = random.choice(quotes) + "\n"

conn.sendall(quote.encode())

conn.close()

s.close()
