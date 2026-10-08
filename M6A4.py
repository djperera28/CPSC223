## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 6 Assignment 4

def show_messages(messages_list):
    while messages_list:
        messages_list.copy()
        print(messages_list.pop())

my_messages = []
my_message = input("What is the next message? (type 'q' to quit) ")
while my_message != 'q':
    my_messages.append(my_message)
    my_message = input("What is the next message? (type 'q' to quit) ")
print("First time calling function")
show_messages(my_messages.copy())
print("Second time calling function")
show_messages(my_messages)