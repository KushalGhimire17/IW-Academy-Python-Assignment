sample_list = [
    {"name": "Kushal", "age": 24},
    {"name": "Kiran", "age": 22},
    {"name": "Karan", "age": 26},
    {"name": "Kapil", "age": 26}
]

def sort_list_of_dict(sample_list):
    print("The list printed sorting by age: ")
    print(sorted(sample_list, key = lambda i: i['age']))
    print("\r")

    print("The list printed sorting by age and name: ")
    print(sorted(sample_list, key = lambda i: (i['age'], i['name']))) 
    print("\r")

    print("The list printed sorting by age in descending order: ")
    print(sorted(sample_list, key = lambda i: i['age'],reverse=True))

sort_list_of_dict(sample_list)