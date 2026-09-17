## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 3 Assignment 6

s_name = input("What is the student name? ")
s_score = int(input("What is their score? "))

if s_score >= 90:
    print(f"{s_name} earned an A")
elif s_score >= 80:
    print(f"{s_name} earned a B")
elif s_score >= 70:
    print(f"{s_score} earned a C")
elif s_score >= 60:
    print(f"{s_score} earned a D")
else:
    print(f"{s_score} earned an F")