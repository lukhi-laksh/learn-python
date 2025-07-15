def targets(arr, index, n, target):
    if target == 0:
        return 1
    if index == n or target < 0:
        return 0
    
    return targets(arr, index+1, n, target) or targets(arr, index+1, n, target - arr[index])


arr = [3, 6, 4, 5, 6]
index = 0
n = len(arr)
target = 5
print(targets(arr, index, n, target))