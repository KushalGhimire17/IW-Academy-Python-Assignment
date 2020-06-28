sample_list = [1,2,3,4,5,6,7,8,9,10]

def filter_list(sample_list):
    print("Original list of integers:")
    print(sample_list)
    print("\r")

    print("\nEven numbers from the sample list:")
    even_numbers_list = list(filter(lambda x: x%2 == 0, sample_list))
    print(even_numbers_list)
    print("\r")

    print("\nOdd numbers from the sample list:")
    odd_numbers_list = list(filter(lambda x: x%2 != 0, sample_list))
    print(odd_numbers_list)

filter_list(sample_list)