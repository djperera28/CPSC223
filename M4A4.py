## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 4 Assignment 4

guy_dict1 = {
    'name': 'Jimmer',
    'age': 23,
    'scout rank': 'Eagle',
    'scout badges': []
}

print("I know Jimmer has three scout badges, what are they? ")
badge1 = (input("The first badge is: "))
badge2 = (input("The second badge is: "))
badge3 = (input("The third badge is: "))

guy_dict1['scout badges'] = [badge1, badge2, badge3]
print(guy_dict1)


