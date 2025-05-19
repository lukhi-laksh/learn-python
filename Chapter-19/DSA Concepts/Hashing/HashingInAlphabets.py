def countAppears(arr):
    count = 0
    prr = [0] * 26

    for i in range(len(arr)):
        index = ord(arr[i]) - 97
        prr[index] += 1
    return prr

arr = ['a', 'c', 'j', 'b', 'b', 'b', 'a', 'z']
print(countAppears(arr))