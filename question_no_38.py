sample_dict = {'one': 1, 'two': 4, 'three': 9}
del_key = input("Enter key to delete: ")

try:
    del sample_dict[del_key]
except KeyError:
    print("Key: '{}' is not in dictionary.".format(del_key))

print("Dictionary: ",sample_dict)