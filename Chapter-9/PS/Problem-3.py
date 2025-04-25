with open("Problem-2.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)