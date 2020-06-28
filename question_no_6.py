try:
    user_input = input("Enter a string: ")
    index_not = user_input.index("not")
    index_poor = user_input.index("poor")

    #driver logic
    if "not" and "poor" in user_input and index_poor > index_not:
        updated_string = user_input[:index_not] + 'good' + user_input[(index_poor+4):]
        print(updated_string)
    else:
        print("The index of 'poor' is less than 'not'.")

except(ValueError):
    print("Either 'not' or 'poor' or both missing in the string.")