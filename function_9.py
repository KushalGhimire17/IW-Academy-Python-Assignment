user_input = int(input("Enter a number: "))

def check_prime(number):
    if number > 1:
        for num in range(2, number):
            if(number % num) == 0:
                print(number,"is not a prime number")  
                print(num,"times",number//num,"is",number)  
                break  
        else:  
            print(number,"is a prime number")  
                    
    else:  
        print(number,"is not a prime number")      

check_prime(user_input)