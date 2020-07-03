"""Calculate average age and printing name
"""

list_of_tuples = []

#append tuple to list
first_name, last_name, age = "Kushal", "Ghimire", 24
list_of_tuples.append((first_name, last_name, age))

first_name, last_name, age = "Bikash", "Rai", None
list_of_tuples.append((first_name, last_name, age))

first_name, last_name, age = "Diwash", "Khanal", 22
list_of_tuples.append((first_name, last_name, age))

first_name, last_name, age = "Pradeep", "Dahal", 28
list_of_tuples.append((first_name, last_name, age))

print(list_of_tuples)

#calculate average age
sum_list = []
length = len(list_of_tuples)
for value in list_of_tuples:
    if value[2] is not None:
        sum_list.append(value[2])
    else:
        length -= 1
print(length)
average_age = sum(sum_list)/length 
print(average_age) 

#print the name and age
for value in list_of_tuples:
    if value[2] is not None:
        if value[2] > average_age:
            print("Name: {}[{}] is older than average age[{}]".format(value[0],value[2],average_age))
        elif value[2] < average_age:
            print("Name: {}[{}] is younger than average age[{}]".format(value[0],value[2],average_age))
        else:
            print("Name: {}[{}] is equal to average age[{}]".format(value[0],value[2],average_age))