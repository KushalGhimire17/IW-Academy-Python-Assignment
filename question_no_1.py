import collections

user_input = input("Enter a string to count the number of characters : ")
frequencies = collections.Counter(user_input)
repeated = {}

for key, value in frequencies.items():
    repeated[key] = value

print(repeated)