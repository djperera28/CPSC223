## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 10 Assignment 1

import socket

print("Welcome to the chatBOT 3000 Client.")
port = int(input("What is the connecting port: "))

s = socket.socket()
s.connect(('127.0.0.1', port))

while True:
    message = input("Enter message (type 'q' to quit): ")
    s.send(message.encode())
    if message == 'q':
        break
print("chatBOT 3000 client out.")