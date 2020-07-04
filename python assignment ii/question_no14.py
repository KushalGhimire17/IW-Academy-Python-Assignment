"""read a csv file
"""
import csv 

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        output_list = []
        for row in reader:
            value = {'username':row["username"], 'address':row["address"], 'age':row["age"]}
            output_list.append(value)

        return output_list
print(read_csv('test.csv'))