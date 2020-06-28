def insert_string_middle(destination,source):
    print(destination[:2] + source + destination[2:])

source = input("Enter the word such as Python : ")
destination = input("Enter the string such as [[]] : ")
insert_string_middle(destination,source)