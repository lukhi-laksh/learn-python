def countAppears(num, arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == num:
            count += 1
    return count

num = 1
arr = [1, 2, 5, 2, 3, 2, 6, 1]
print(countAppears(num, arr))