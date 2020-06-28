ans = 'y'
small_list = []
while ans.casefold() == 'y':
    user_input = int(input("Enter the amount to be added in list."))
    ans = input("Do you want to add more [y/n]?")
    small_list.append(user_input)

result = small_list[0]
for num in small_list:
    if num < result:
        result = num
print("The smallest number is {}".format(result))