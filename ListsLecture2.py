new_list = ["In", "brightest", "day", "in", "blackest", "night", "no", "evil", "shall"]

for word in new_list:
    print(f"This word is: {word}")
    print(f"This word in upper: {word.upper()}")
    print(f"This word in lower: {word.lower()}")
    print(f"This word in title: {word.title()}")
    print(f"The type of word is {type(word)}")

new_string = "This is an example of a title"
print(new_string.title())

num_list = list(range(1,100,2))         # range is inclusive of the first number and exclusive of the last number
sum = 0                           # (start, stop, step)
for num in num_list:
    print(f"The number is {num}")
    sum += num
    print(f"The current sum is {sum}")
print(f"The average value is {sum / len(num_list)}")

list1 = [1, 2, 3]
list2 = []
for element in list1:
    list2.append(element)
list1 = [4, 5, 6]

print(list1)
print(list2)