user_input = input("Enter a string: ")
last_char = user_input[-1:]
first_char = user_input[:1]

updated_string = last_char + user_input[1:-1] + first_char
print("{0} is swapped with {1} to give {2}".format(first_char,last_char,updated_string))
