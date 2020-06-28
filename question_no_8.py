user_string_input = ""
while user_string_input == "":
    user_string_input = input("Enter a string: ")
    continue
print("\nNumber of characters in '{}' are: {}".format(user_string_input,len(user_string_input)))

try:
    user_remove_input = int(input("\nEnter index no to remove a character: "))
    if user_remove_input > len(user_string_input) -1:
        print("\nThe valid index is from 0 to {0}".format(len(user_string_input)-1))
    else:
        output = user_string_input[:user_remove_input] + user_string_input[user_remove_input+1:]
        print("\nOutput: {}".format(output))

except(ValueError):
    print("\nInvalid index...")