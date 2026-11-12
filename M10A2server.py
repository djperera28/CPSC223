## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 10 Assignment 2

import socket

print("Welcome to the chatBOT 5000 server.")
port = int(input("What is the listening port: "))

s = socket.socket()
s.bind(('', port))
s.listen(1)

c, addr = s.accept()
while True:
    message = c.recv(1024).decode()
    if message == 'q':
        break
    print(f"The client said: {message}")
    print(f"Sending back: {message.upper()}")
    c.send(message.upper().encode())

c.close()
s.close()
print("chatBOT 5000 server out.")