## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 3 Assignment 5

start_int = int(input("What is the first number? "))
end_int = int(input("What is the second number? "))

num_list = list(range(start_int, end_int+1))
sum_int = 0
for sum in num_list:
    if (sum % 5) == 0:
        sum_int += sum

print(f"The total value of multiples of 5 from {start_int} to {end_int} is {sum_int}")