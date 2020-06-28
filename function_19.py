from functools import reduce
user_input = int(input("Enter the value of n: "))

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1]) 
  
print(fib(user_input)) 