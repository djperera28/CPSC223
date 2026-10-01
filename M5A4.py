## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 5 Assignment 4

orders_list = ['pastrami', 'turkey', 'pastrami', 'ham', 'turkey']
finished_list = []

while orders_list:
    sandwich = orders_list.pop()
    finished_list.append(sandwich)
    print(f"I made your {sandwich}")
print(f"Here are all the sandwiches I made: ")
for sandwich in finished_list:
    print(f"{sandwich}")