ans = 'y'
large_list = []
while ans.casefold() == 'y':
    user_input = int(input("Enter the amount to be added in list."))
    ans = input("Do you want to add more [y/n]?")
    large_list.append(user_input)

result = 0
for num in large_list:
    if num > result:
        result = num
print("The largest number is {}".format(result))