## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 9 Assignment 2

starting_string = """Print this in uppercase
Print this in lowercase
Print this as a title
Print this left justified (80 characters, with ='s)
Print this right justified (80 characters, with +'s)"""

lines_of_text = starting_string.splitlines()

print(lines_of_text[0].upper())
print(lines_of_text[1].lower())
print(lines_of_text[2].title())
print(f"{lines_of_text[3]:=<80}")
print(f"{lines_of_text[4]:+>80}")

print(";".join(lines_of_text))

second_j = starting_string.index("j", starting_string.index("j") + 1)
print(starting_string[second_j:second_j + 5])
