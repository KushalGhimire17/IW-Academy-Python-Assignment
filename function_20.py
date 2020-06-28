array_nums1 = [1, 2, 3, 4, 5]
array_nums2 = [1, 3, 5, 7, 9]
print("Original arrays:{} and {}".format(array_nums1, array_nums2))

result = list(filter(lambda x: x in array_nums1, array_nums2)) 
print ("\nIntersection of the arrays: ",result)