def countAppears(arr):
    count = 0
    prr = [0] * 26

    for i in arr:
        prr[ord(i) - ord('a')] += 1
    return prr

arr = "abaaccbaazehsd"
print(countAppears(arr))