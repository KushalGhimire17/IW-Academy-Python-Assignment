def check_if_number(string):
    is_number = lambda x: True if x.isnumeric() else False
    print(is_number(string))

check_if_number('123')  #true
check_if_number('kush') #false