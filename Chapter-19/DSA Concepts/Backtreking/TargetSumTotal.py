def targets(arr, index, n, target):

    if index == n:
        return target == 0
    
    return targets(arr, index+1, n, target) + targets(arr, index+1, n, target - arr[index])


arr = [1, 0]
index = 0
n = len(arr)
target = 1
print(targets(arr, index, n, target))