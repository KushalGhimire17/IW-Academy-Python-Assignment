original_tuple = ('9','8','4','7','6','2','1') 
user_input = input("Enter an item to delete from a tuple: ")
index_of_item = original_tuple.index(user_input)
print(index_of_item)

if user_input in original_tuple:
    original_tuple = original_tuple[:index_of_item] + original_tuple[index_of_item+1:]

print(original_tuple)