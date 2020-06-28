sample_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
mul_of_values = 1
# sample_dict = {'one': 1, 'two': 4, 'three': 9}

for value in sample_dict:
    mul_of_values *= sample_dict[value]

print(mul_of_values)