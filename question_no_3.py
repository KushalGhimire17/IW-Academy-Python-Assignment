user_input = input("Enter a string : ")

char = user_input[0]
user_input = user_input.replace(char, "$")
user_input = char + user_input[1:]
print(user_input)