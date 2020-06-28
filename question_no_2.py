user_input = input("Enter a string: ")
length = len(user_input)

if length > 2:
    output = user_input[0:2] + user_input[-2:]
    print(output)
elif length == 2:
    output = user_input[0:2] * 2
    print(output)
else:
    print("Empty String")