try:
    a = int(input("Enter any number"))
    print(a)
except ValueError as V:
    print("rewrite name")
    print(V)
finally:
    print("Now you are inside finally")