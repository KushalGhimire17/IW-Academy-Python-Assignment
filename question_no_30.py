dic = {'one': 1, 'two': 2, 'three': 3}
user_input = input("Enter a key: ")

for key, value in dic.items():
    if key == user_input:
        print("The key = {} already exists.".format(key))