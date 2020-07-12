"""Binary Search
"""

def binary_search(element_list, item):
    low = 0
    high = len(element_list) - 1
    mid = 0

    while low <= high:
        mid = low + (high - low)//2

        if element_list[mid] < item:
            low = mid +1
        elif element_list[mid] > item:
            low = mid -1
        else:
            return mid
    else:
        return -1

# driver code
element_list = [10,14,19,27,33,35,42,44]

user_input = int(input("Enter an integer value to see if it exits: "))
  
result = binary_search(element_list, user_input) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 
