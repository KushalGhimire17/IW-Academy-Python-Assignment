"""Basic calculator
"""  
def calculator(number1, number2, operator):
    if operator == '+':
        return number1 + number2

    elif operator == '-':
        return number1 - number2

    elif operator == '*':
        return number1 * number2

    elif operator == '/':
        try:
            return number1 / number2
        except ZeroDivisionError:
            print("Cant divide by zero..")
    else:
        print("Invalid operator")

# driver code
ans = 'y'
while ans.casefold() == 'y':
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        operator = input("Enter an operator [+, -, *, /]: ")

    except ValueError or NameError:
        print("Value error")
        if NameError:
            break

    print(calculator(number1, number2, operator))
    ans = input("CONTINUE [y/n]? ")