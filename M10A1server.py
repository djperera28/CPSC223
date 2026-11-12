## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 10 Assignment 1

import socket

print("Welcome to the chatBOT 3000 server.")
port = int(input("What is the listening port: "))

s = socket.socket()
s.bind(('127.0.0.1', port))
s.listen(1)

c, addr = s.accept()
while True:
    message = c.recv(1024).decode()
    if message == 'q':
        break
    print(f"The client said: {message}")


c.close()
s.close()
print("chatBOT 3000 server out.")