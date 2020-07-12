"""Insertion sort maintains a sublist which is always sorted
   1. Using while loop
"""

# def insertion_sort(element_list):
#     length_of_list = len(element_list)

#     for i in range(1, length_of_list):
#         j = i -1 
#         while j >= 0 and element_list[j] > element_list[j+1]:
#             element_list[j], element_list[j+1] = element_list[j+1], element_list[j]
#             j -= 1

# element_list = [14,33,27,10,35,19,42,44]
# insertion_sort(element_list)

# print("After insertion sort: ")
# for i in range(len(element_list)):
#     print(element_list[i])

"""2. Using nested for loop and swapping
"""
def insertion_sort(array_of_number):
    for i in range(1, len(array_of_number)):
        #j is ranged from i-1 to 0 to indicate "ELEMENTS LEFT OF I"
        for j in range(i-1, 0, -1):
            if array_of_number[j-1] > array_of_number[j]:
                array_of_number[j-1], array_of_number[j] = array_of_number[j], array_of_number[j-1]
            else:
                break
    print("After insertion sort: ")
    for i in range(len(array_of_number)):
        print(array_of_number[i])

element_list = [14,33,27,10,35,19,42,44]
insertion_sort(element_list)