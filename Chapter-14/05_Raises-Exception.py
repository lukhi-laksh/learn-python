a = int(input("Enter first number"))
b = int(input("Enter second number"))

if (b == 0):
    raise ZeroDivisionError("hey our progream is not meant to devide number by zero")
else:
    print(f"The deveiseon of a and b is {a/b}")