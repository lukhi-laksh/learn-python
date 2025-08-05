def way (arr, n, sum):
    # Base case
    if sum == 0:
        return 1
    # Second base case
    if sum < 0:
        return 0

    # Declare sum = 0
    ans = 0
    for i in range(n):
        ans += way (arr, n, sum - arr[i])
    
    return ans
    
arr = [1, 5, 6]
target = 7
n = len(arr)
print(way(arr, n, target))
