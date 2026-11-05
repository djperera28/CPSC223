## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 9 Assignment 1

population_dict = {}

city = input("What is the next city? (enter q to quit) ")
while city != 'q':
    population = int(input(f"What is the population of {city}? "))
    population_dict[city] = population
    city = input("What is the next city? (enter q to quit) ")

population_data = int(input("What is the largest population for a small town? "))

with open("populationdata.txt", "w") as file_object:
    print("Big Cities:", file=file_object)
    for city, population in population_dict.items():
        if population > population_data:
            print(f"{city},{population}", file=file_object)

    print("Small Towns:", file=file_object)
    for city, population in population_dict.items():
        if population <= population_data:
            print(f"{city},{population}", file=file_object)
