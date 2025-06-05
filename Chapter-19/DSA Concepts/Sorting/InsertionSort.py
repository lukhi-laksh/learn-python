arr = [7, 4, 2, 3, 5]

for i in range(len(arr) - 1):
    for j in range(len(arr) - 1, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]

print(arr)