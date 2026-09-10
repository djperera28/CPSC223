## Name: David Perera
# Student ID: 884532367
# Section: 07 
# Assignment: Module 2 Assignment 3

uber_list = list(range(100,201,2))

start = int(input("What is the start of your slice? "))
end = int(input("What is the end of your slice? "))
uber_list[start:end]

data_list = uber_list[start:end]
total_int = 0
for avg in data_list:
    total_int += avg
print(f"Your slice contains {len(data_list)} values and has an average value of {total_int / len(data_list)}")