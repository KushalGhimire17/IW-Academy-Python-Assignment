"""Linear search
"""

def linear(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

#driver code
arr = [14,33,27,10,35,19,42,44]
print("Index: ",linear(arr,10))