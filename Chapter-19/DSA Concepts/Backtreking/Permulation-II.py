def permute(arr, ans, index):
    
    if index == len(arr):
        ans.append(arr[:])
        return
    
    use = [0] * 21
    for i in range(index, len(arr)):
        if use[arr[i]] + 10 == 1:
            continue

            

arr = [1, 1, 2]
ans = []
index = 0
permute(arr, ans, index)
print(ans)