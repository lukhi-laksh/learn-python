arr = [0, 1, 0, 1, 0, 1]

count0 = 0
count1 = 0
for i in arr:
    if i == 0:
        count0 += 1
    else:
        count1 += 1
for i in range(count0):
    arr[i] = 0
for j in range(count0, len(arr)):
    arr[j] = 1

print(arr)