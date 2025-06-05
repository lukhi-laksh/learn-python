arr = [2, 5, 4, 7, 9, 11, 13]
target = 15
empty = set()
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            empty.add((i,j))
            
print(empty)