def laksh(arr, n):
    if n == 0:
        return arr[0]
    
    return arr[n] + laksh(arr, n - 1)


arr = [3, 4, 5, 8, 2, 3]
print(laksh(arr, len(arr) - 1))