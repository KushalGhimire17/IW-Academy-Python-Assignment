"""Bubble sort sorts one number on each pass i.e. highest number is on its correct place on every pass.
"""

def bubble_sort(element_list):
    length_of_list = len(element_list)

    for i in range(length_of_list):
        for j in range(0, length_of_list-i-1):
            if element_list[j] > element_list[j+1]:
                element_list[j], element_list[j+1] = element_list[j+1], element_list[j]

element_list = [14,33,27,35,10]
bubble_sort(element_list)

print("After bubble sort: ")
for i in range(len(element_list)):
    print("%d" %element_list[i])