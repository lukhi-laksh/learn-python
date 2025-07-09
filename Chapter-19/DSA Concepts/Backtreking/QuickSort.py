def partition(arr, start, end):
    pos = start
    for i in range(start, end + 1):
        if arr[i] <= arr[end]:
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1
    return pos - 1


def QuickSort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        QuickSort(arr, start, pivot - 1)
        QuickSort(arr, pivot + 1, end)


arr = [6, 4, 2, 8, 13, 7, 11, 9, 3, 6]
QuickSort(arr, 0, len(arr) - 1)
print(arr)
