def way (arr, n, sum):
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    
    ans = 0
    for i in range(n):
        ans += way (arr, n, sum - arr[i])
    
    return ans
    
arr = [1, 5, 6]
target = 7
n = len(arr)
print(way(arr, n, target))