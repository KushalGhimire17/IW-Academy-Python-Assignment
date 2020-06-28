string_list = []
ans = 'y'
while ans.casefold() == 'y':
    user_input = input("Enter a string: ")
    ans = input("Do you want to add more [y/n]?")
    string_list.append(user_input)

count = 0
for string in string_list:
    if ((len(string) >= 2) and (string[:1] == string[-1:-2:-1])):
        count += 1

print(count)