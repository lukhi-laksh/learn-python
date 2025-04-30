n = int(input("Enter a number you want to table"))

table = [n*i for i in range(1, 11)]
with open("table.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")