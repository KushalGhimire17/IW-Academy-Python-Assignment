""" camelcase to snake_case
"""

def change_case(string):
    snake_case = ''.join(['_' + i.lower() if i.isupper()
                    else i for i in string]).lstrip('_')
    return snake_case

user_input = input("Enter CamelCase string: ")
print(change_case(user_input))