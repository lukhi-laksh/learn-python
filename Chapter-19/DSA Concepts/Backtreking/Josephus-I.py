def winner(arr, n, index, left, k):
    if left == 1:
        for i in range(n):
            if arr[i] == 0:
                return i
    
    kill = (k - 1) % left

    # kill --
    while kill:
        index = (index + 1) % n
        while arr[index] == 1:
            index = (index + 1) % n
        kill -= 1

    # Index value set
    while arr[index] == 1:
        index = (index + 1) % n

    arr[index] = 1

    # Set Index Value
    index = (index + 1) % n
    while arr[index] == 1:
        index = (index + 1) % n

    # Backtraking
    return winner(arr, n, index, left - 1, k)


arr = [0] * 5
n = len(arr)
index = 0
left = n
k = 2

print("Winner is at index:", winner(arr, n, index, left, k))
