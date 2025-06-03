def reverse(i, arr, n):
    if i >= n // 2:
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    reverse(i + 1, arr, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
reverse(0, arr, len(arr))
print(arr)