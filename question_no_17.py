ans = 'y'
product_list = []
while ans.casefold() == 'y':
    user_input = int(input("Enter the amount to be added in list."))
    ans = input("Do you want to add more [y/n]?")
    product_list.append(user_input)

result = 1
for num in product_list:
    result *= num
print("The product is {}".format(result))