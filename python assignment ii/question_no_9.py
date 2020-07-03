"""Binary search function
"""

def binary_search(sequence, item):

    #initialization yo avoid garbage value in variable
    high = len(sequence) - 1
    low = 0
    mid = 0

    while low <= high:

        mid = (high + low) // 2
  
        if arr[mid] < item: 
            low = mid + 1
  
        elif arr[mid] > item: 
            high = mid - 1
  
        else: 
            return mid

    else:  
        return -1
  
# Sample test array 
arr = [ 2, 3, 4, 10, 40 ] 
user_input = int(input("Enter an integer value to see if it exits: "))
  
result = binary_search(arr, user_input) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 