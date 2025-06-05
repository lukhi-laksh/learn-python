arr = [2, 4, 5, 7, 9, 11, 13]
target = 15
start = 0
end = len(arr) - 1
while start < end:
    if arr[start] + arr[end] == target:
        print(start, end)
        start += 1
        end -= 1
    elif arr[start] + arr[end] > target:
        end -= 1
    elif arr[start] + arr[end] < target:
        start += 1
    else:
        print("value not found")