def permute(arr, index, result):

    if index == len(arr):
        result.append(arr[:])
        return
    
    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]
        permute(arr, index + 1, result)
        arr[index], arr[i] = arr[i], arr[index]


arr = [1, 2, 3]
result = [] 
permute(arr, 0, result)
print(result)
