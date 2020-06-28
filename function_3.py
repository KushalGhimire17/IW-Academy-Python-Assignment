sample_list = [8,2,3,1,7]

def mul_from_list(sample_list):
    result = 1
    for item in sample_list:
        result *= item
    return result

print("The multiplication from list is: ",mul_from_list(sample_list))
