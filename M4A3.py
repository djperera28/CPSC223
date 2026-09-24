## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 4 Assignment 3

games_dict = {}

for item in range(3):
    game = input("What is a great game? ")
    system = input("What system can I play that on? ")
    games_dict[game] = system

print("That's too many, let's get rid of one")
del games_dict[(input("What game should we remove? "))]
print("The new dictionary is: ")

for items in games_dict:
    print(f"You can play {items} on {games_dict[items]}")