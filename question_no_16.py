ans = 'y'
sum_list = []
while ans.casefold() == 'y':
    user_input = int(input("Enter the amount to be added in list."))
    ans = input("Do you want to add more [y/n]?")
    sum_list.append(user_input)

result = 0
for num in sum_list:
    result += num
print("The sum is {}".format(result))