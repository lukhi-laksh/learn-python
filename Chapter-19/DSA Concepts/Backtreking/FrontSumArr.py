def laksh(arr, n):
    # base Case
    if n == 0:
        # Return array first index
        return arr[0]

    # Function Recall
    return laksh(arr, n - 1) + arr[n]

# Define list
arr = [3, 4, 5, 8, 2, 3]
print(laksh(arr, len(arr) - 1))
