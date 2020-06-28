sample_list = [1,2,3,4,5,6,7,8,9]

def display_even(number_list):
    even_list = []
    for number in number_list:
        if number%2 == 0:
            even_list.append(number)
    return even_list

print(display_even(sample_list))