string = input("Enter the input without space: ")

#Converting into list
new_list = string.split(",")

#Sorting in alphabetical order 
new_list.sort()

#Removing duplicate
final_list = []

for x in new_list:
	if x not in final_list:
		final_list.append(x)

final_string = ",".join(final_list)


#Final result
print(final_string)