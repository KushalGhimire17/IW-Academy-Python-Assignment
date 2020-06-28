x = int(input("Enter a number[x]: "))
y = int(input("Enter a number[y]: "))

add = lambda number: number + 15
mul = lambda x,y: x*y

print("ADD",add(x))
print("MUL",mul(x,y))