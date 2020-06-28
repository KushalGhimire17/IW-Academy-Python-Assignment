string_list = []
ans = 'y'
while ans.casefold() == 'y':
    user_input = input("Enter an item : ")
    ans = input("Do you want to add more [y/n]?")
    string_list.append(user_input)

cloned_list = string_list.copy()
print("Orginal list: {}".format(string_list))
print("Cloned list: {}".format(cloned_list))