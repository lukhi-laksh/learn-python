def laksh(arr, n):
    if n == -1:
        return

    print(arr[n])
    laksh(arr, n - 1)



arrays = [2, 65, 23, 34, 23, 6]
laksh(arrays, len(arrays)-1)