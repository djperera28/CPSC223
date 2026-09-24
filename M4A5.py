## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 4 Assignment 5

food_dict = {'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
             }

for name, favorite_food in food_dict.items():
    if favorite_food == '':
        food_dict[name] = input(f"What is {name}'s favorite food? ")

print("Here are the favorite foods: ")
for items in food_dict:
    print(f"{items}'s favorite food is {food_dict[items]}")