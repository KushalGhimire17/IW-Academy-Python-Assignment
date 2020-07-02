"""sorting a list of tuple
"""
# itemgetter is faster than lambda function since almost all of the computation will be done on the C side.
from operator import itemgetter

# my tuple
firstname, lastname, age = ("Kushal", "Ghimire", 24)
# create a list
people = []
# append your tuple
people.append((firstname, lastname, age))
# make more tuples andappend to the list
firstname, lastname, age = ("Kush", "Sapkota", 20)
people.append((firstname, lastname, age))

firstname, lastname, age = ("Bikash", "Rai", 26)
people.append((firstname, lastname, age))
print("ORIGINAL LIST: ", people)
print()

# sort the list with firstname
# sorted_list = sorted(people, key=lambda x: x[0])
sorted_list = sorted(people, key=itemgetter(0))
print("FIRSTNAME: ", sorted_list)
print()

# sort the list with lastname
sorted_list = sorted(people, key=itemgetter(1))
print("LASTNAME: ", sorted_list)
print()

# sort the list with age
sorted_list = sorted(people, key=itemgetter(2))
print("AGE: ", sorted_list)