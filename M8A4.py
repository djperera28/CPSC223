## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 8 Assignment 4

def dictionary_maker(file_path):
    ret_dict = {}
    try:
        with open(file_path, "r") as file_object:
            for line in file_object:
                key, value = line.strip().split(": ", 1)
                ret_dict[key] = value
    except FileNotFoundError:
        print(f"The file {file_path} does not exist on this system")
    return ret_dict


file_name = input("What is the file with the data? ")
print(dictionary_maker(file_name))
