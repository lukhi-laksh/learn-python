def laksh(arr, index):
    if index == -1:
        return

    laksh(arr, index - 1)
    print(arr[index])

arr = [5, 6, 8, 6]
laksh(arr, len(arr) - 1)