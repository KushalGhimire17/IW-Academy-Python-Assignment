user_input = input("Enter a string: ")

#whole string to list
user_input_list = list(user_input)
#last three items of list to string
ing_check_string = "".join(user_input_list[-3:])

if len(user_input) >= 3:
    if ing_check_string == "ing":
        user_input_list += "ly"
        output = "".join(user_input_list)
        print(output)
    else:
        user_input_list += "ing"
        output = "".join(user_input_list)
        print(output)
else:
    print(user_input)