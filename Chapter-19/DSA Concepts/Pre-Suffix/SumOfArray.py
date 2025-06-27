arr = [6, 4, 5, -3, 2, 8]

empty = [None] * len(arr)
revEmpty = [None] * len(arr)

empty[0] = arr[0]
revEmpty[len(arr)-1] = arr[len(arr)-1]



for i in range(1, len(arr)):
    empty[i] = empty[i - 1] + arr[i]
print(empty)

for i in range(len(arr) - 2, -1, -1):
    revEmpty[i] = revEmpty[i + 1] + arr[i]
print(revEmpty)