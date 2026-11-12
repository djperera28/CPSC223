## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 10 Assignment 2

import socket

print("Welcome to the chatBOT 5000 Client.")
ip = input("What is the connecting IP address: ")
port = int(input("What is the connecting port: "))

s = socket.socket()
s.connect((ip, port))

while True:
    message = input("Enter message (type 'q' to quit): ")
    s.send(message.encode())
    if message == 'q':
        break
    response = s.recv(1024).decode()
    print(f"Server sent back: {response}")

s.close()
print("chatBOT 5000 client out.")