arr = [9, 5, 8, 12, 2, 3, 7, 4]
ans = -2**35 - 1
subfix = arr[len(arr)-1]

for i in range(len(arr)-2, -1, -1):
    ans = max(subfix - arr[i], ans)
    
    if subfix < arr[i]:
        subfix = arr[i]
    
print(ans)
    