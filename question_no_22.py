string_list = []
ans = 'y'
while ans.casefold() == 'y':
    user_input = input("Enter an item : ")
    ans = input("Do you want to add more [y/n]?")
    string_list.append(user_input)

print(string_list)
list_updated = list(dict.fromkeys(string_list))
print(list_updated)