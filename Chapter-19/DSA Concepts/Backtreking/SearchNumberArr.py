def laksh(arr, l, x):
    if arr[l] == x:
        return l
    
    if l < 0:
        return -1
    
    return laksh(arr, l - 1, x)


arr = [2, 6, 8, 4, 1, 7]
x = 7
print(laksh(arr, len(arr) - 1, x))