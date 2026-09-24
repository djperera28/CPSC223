## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 4 Assignment 1

g_list = []

for game in range(3):
    game = g_list.append(input(f"What is your number {game+1} favorite Playstation game? "))

for index, game in enumerate(g_list, start = 1):
    print(f"Your number {index} favorite game was {game}")

