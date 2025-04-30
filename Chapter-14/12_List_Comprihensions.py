myList = [1, 2, 5, 9, 6, 8]

squaredlsit = []

for item in myList:
    squaredlsit.append(item * item)

print(squaredlsit)


# Best way to do same thing

squaredlsit = [i * i for i in myList]
print(squaredlsit)