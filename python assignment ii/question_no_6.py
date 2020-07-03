"""Searching name using for loop
"""

sample_list = ["Kushal", "John", "Bikash", "Paras", "Pradeep", "Diwash"]
print(sample_list)

for name in sample_list:
    if name == 'John':
        print("Found...")
    else:
        print("Not found...")