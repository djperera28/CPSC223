num_list = list(range(0,100))

print(num_list)

print(num_list[2:9])            #slicing, inclusive of the first index and exclusive of the last index 
print(num_list[2:])
print(num_list[:9])
new_list = num_list[:]          # copy of the list
new_list[0] *= 2
new_list[1] *= 2
new_list[2] *= 2

print(f"The original list is:")
print(num_list)
print(f"The new list is:")
print(new_list)

print(num_list[5:-2])                       # goes from 5 to the second to last index