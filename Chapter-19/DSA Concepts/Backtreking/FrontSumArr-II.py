def laksh(arr, n):
    # Base Condition
    if n == len(arr) - 1:
        return arr[len(arr) - 1]
    
    # Function Recall
    return arr[n] + laksh(arr, n + 1)


arr = [3, 4, 5, 8, 2, 3]
print(laksh(arr, 0))