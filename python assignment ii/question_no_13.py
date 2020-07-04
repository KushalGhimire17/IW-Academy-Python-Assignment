"""CSV creation
"""
import csv

def write_csv(filename,list_of_tuples):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['username', 'address', 'age']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in list_of_tuples:
            (username, address, age) = item
            writer.writerow({'username':username, 'address':address, 'age':age})

list_of_tuples = [('Kush', 'Bairiya', 24), ('Test', 'Pokhara', 48)]
write_csv('test.csv',list_of_tuples)