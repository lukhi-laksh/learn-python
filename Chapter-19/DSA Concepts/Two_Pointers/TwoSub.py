arr = [5, 4, 3, 2, 1]
target = 2

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] - arr[j] == target:
            print(i, j)
        