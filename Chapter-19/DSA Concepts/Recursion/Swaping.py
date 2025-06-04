def swaping(p, arr, n):
    if p >= n:
        return
    arr[p] , arr[n] = arr[n] , arr[p]
    return swaping(p + 1, arr,  n - 1)

arr = [2, 3, 4, 5, 6, 7, 8]
print(swaping(0, arr, len(arr) - 1))
print(arr)