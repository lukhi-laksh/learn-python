a = "aabbggggggksjshgsh"

empty = {}

for val in a:
    if val in empty:
        empty[val] += 1
    else:
        empty[val] = 1
for val in empty:
    if empty[val] == 2:
        print(empty[val])
print(empty)