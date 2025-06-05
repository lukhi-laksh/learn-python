arr = [0, 1, 0, 1, 0, 1]

a = 0
b = len(arr) - 1

for i in range(len(arr)//2):
    if arr[a] == 1 and arr[b] == 0:
        arr[a] , arr[b] = arr[b], arr[a]
        a += 1
        b -= 1
    else:
        a += 1
        b -= 1

print(arr)