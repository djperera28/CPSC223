## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 6 Assignment 1

def favorite_book(title):
    title = input(f"What is your favorite book? ")
    return title

for book in range(3):
    book = favorite_book(book)
    print(f"One of my favorite books is {book}")