## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 8 Assignment 3


while True:
    first_num = input("What is the first number? (or q to quit) ")
    if first_num == "q":
        print("The program is over")
        break

    second_num = input("What is the second number? ")
    try:
        answer = float(first_num) / float(second_num)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"{first_num} / {second_num} is {answer}")