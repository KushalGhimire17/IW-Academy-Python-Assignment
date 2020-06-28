my_dict = {0: 10, 1: 20}

key = int(input("Enter a new int key: "))
value = int(input("Enter an int value to key = {}: ".format(key)))
my_dict[key] = value

print("Before: ", my_dict)
print("After: ", my_dict)