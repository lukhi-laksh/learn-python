arr = [7, 4, 6, 9, 3, 5, 6, 2, 4, 6, 7, 6, 4]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the elements

print(arr)
