def laksh(arr):
    if len(arr) == 0:
        return

    print(arr.pop())
    laksh(arr)


arrays = [2, 3, 5, 3, 2, 4]
laksh(arrays)