user_input = input("Enter a string: ")

def reverse(string):
    return user_input[-1::-1]

print(reverse(user_input))