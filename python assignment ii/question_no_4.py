"""Check the id of list
"""

#empty list creation
friend_list = list()
empty_id = id(friend_list)
print("Empty list ID: ", empty_id)

#appending item on list
friend_list.append("Bikash")
friend_list.append("Paras")
friend_list.append("Amit")
after_append_id = id(friend_list)
print("After appending item, ID: ", after_append_id)

#sort the list
friend_list.sort()
sorted_id = id(friend_list)
print("Sorted list ID: ", sorted_id)

print("=="*20)

#driver logic
if empty_id == sorted_id:
    print("The id of a list didn't change !")
else:
    print("The id of a list changed !")

print("=="*20)

print("The first item in the sorted list is {} .".format(friend_list[0]))
print("The second item in the sorted list is {} .".format(friend_list[1]))