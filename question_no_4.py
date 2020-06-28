user_input_1 = input("Enter first string: ")
user_input_2 = input("Enter second string: ")

#list are required as strings are not mutable
list_1 = list(user_input_1)
list_2 = list(user_input_2)
temp_list_1 = []

#swapping logic
temp_list_1 += user_input_1
list_1[0], list_1[1] = list_2[0], list_2[1]
list_2[0], list_2[1] = temp_list_1[0], temp_list_1[1]

#list to string
l1 = "".join(list_1)
l2 = "".join(list_2)

output = l1 + ' ' + l2
print(output)