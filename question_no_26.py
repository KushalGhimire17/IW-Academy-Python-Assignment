sample_list = [1,2,3,4]
user_input = input("Enter a string: ")
output =[]

for item in sample_list:
    result = user_input + str(item)
    output.append(result)

print(output)