arr = [7, 4, 6, 9, 3, 5, 6, 2, 4, 6, 7, 6, 4]

for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)