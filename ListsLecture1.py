my_list = ["I", 2, "ready"]
            #[1, 3, 88]
my_list[-1] = "late"                            # change last item in the list
print(my_list[len(my_list) - 1])
print(f"My list is {len(my_list)} items")         #length of the list

my_list.append("for")
my_list.append("work")
my_list.insert(1, "will")                   # insert an item at a specific index
print(my_list)

print(f"The last item in my list was {my_list.pop()}")  # removes the last item in the list, and returns it      
print(my_list)

del(my_list[-1])
print(my_list)

new_list = ["I", "am", "the", "very", "model", "of", "a", "modern", "general"]
print(new_list)
print(sorted(new_list))             #temporarily sorts the list, but does not change the original list
new_list.sort()                      # sorts the list in place, returns none *which is not the same as null
print(new_list)
new_list.reverse()
print(new_list)