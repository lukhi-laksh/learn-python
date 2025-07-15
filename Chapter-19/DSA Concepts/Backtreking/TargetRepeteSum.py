def targets(arr, index, n, target):
    if target == 0:
        return 1
    if index == n or target < 0:
        return 0
    
    return targets(arr, index+1, n, target) + targets(arr, index, n, target - arr[index])


arr = [2, 3, 4]
index = 0
n = len(arr)
target = 6
print(targets(arr, index, n, target))