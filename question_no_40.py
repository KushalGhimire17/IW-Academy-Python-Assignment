original_tuple = (9,8,4,7,6,2,1) 
print("ID of original tuple: ",id(original_tuple))
print("Original tuple: ", original_tuple)

original_tuple += (9,)
print("ID of modified tuple: ", id(original_tuple))
print("Modified tuple: ",original_tuple)