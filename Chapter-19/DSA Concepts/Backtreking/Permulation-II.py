def permute(arr, ans, index):
    
    if index == len(arr):
        ans.append(arr[:])
        return
    
    use = [0] * 21
    for i in range(index, len(arr)):
        if use[arr[i]] + 10 == 1:
            continue
        use[arr[i] + 10] == 1
        arr[index], arr[i] = arr[i], arr[index]
        permute(arr, ans, index + 1)
        arr[i], arr[index] = arr[i], arr[index]
            

arr = [1, 1, 2]
ans = []
index = 0
permute(arr, ans, index)
print(ans)