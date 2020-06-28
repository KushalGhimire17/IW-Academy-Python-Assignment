user_input = input("Enter a string: ")

def count_character_case(user_input):
    upper_count = 0
    lower_count = 0
    space_count = 0

    for string in user_input:
        if string == ' ':
            space_count += 1
        elif string == string.upper():
            upper_count += 1
        elif string == string.casefold():
            lower_count += 1
        else:
            print("Invalid string")

    print("Number of upper string: ", upper_count)
    print("Number of lower string: ", lower_count)
    print("Number of whitespace string: ", space_count)

count_character_case(user_input)