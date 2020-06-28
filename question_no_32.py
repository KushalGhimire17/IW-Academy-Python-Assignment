number = int(input("Enter an end number: "))
generated_dictionary = {}
key = 1

while key != (number + 1):
    value = key * key 
    generated_dictionary[key] = value
    key += 1
print(generated_dictionary)