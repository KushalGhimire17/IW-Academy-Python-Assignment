sample_list_1 = [{},{},{}]
sample_list_2 = [{},{},{2,3}]

print(all(not d for d in sample_list_1))
print(all(not d for d in sample_list_2))