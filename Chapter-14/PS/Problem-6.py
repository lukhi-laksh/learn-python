try:
    a = int(input("Enter any number"))
    print(a)
except ValueError as V:
    print("I am inside except")
    print(V)
finally:
    print("finally must be run")