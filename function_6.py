number = int(input("Enter a number: "))
start_range = int(input("Enter starting point of range: "))
end_range = int(input("Enter stopping point of range: "))

def test_range(num):
    if num in range(start_range,end_range):
        print( " %s is in the range"%str(num))
    else :
        print("The number is outside the given range.")

test_range(number)