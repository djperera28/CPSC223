## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 3 Assignment 4

current_year = int(input("What year is it now? "))
born_year = int(input("What year were you born? "))

age_int = current_year - born_year

if (age_int % 2) == 0 and age_int < 50:
    print("This will be a great year")
elif (age_int % 2) == 1 and age_int < 50:
    print("This year will be tough")
elif age_int == 50:
    print("The future is unclear")
else:
    print("Death will come for you soon")
