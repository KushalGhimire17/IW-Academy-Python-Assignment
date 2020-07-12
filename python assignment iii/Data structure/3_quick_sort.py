"""Quick sort 
Last element is chosen as pivot. 
"""
def partition(element_list,low,high):
    small = low - 1
    pivot = element_list[high]

    for index in range(low, high):
        if element_list[index] <= pivot:
            small += 1
            element_list[small], element_list[index] = element_list[index], element_list[small]

    element_list[small+1], element_list[high] = element_list[high], element_list[small+1]
    return small+1

def quick_sort(element_list,low,high):
        if low < high:
            partition_index = partition(element_list,low,high)
            #sort before partition
            quick_sort(element_list, low, partition_index-1)
            #sort after partition
            quick_sort(element_list, partition_index+1, high)

element_list = [14,33,27,10,35,19,42,44]
length = len(element_list)
quick_sort(element_list,0,length-1)

print("After quick sort: ")
for i in range(length):
    print(element_list[i])