def TrueHashmap(num, hash):
    arr = [0] * (len(hash))

    for val in hash:
        arr[val] += 1

    return print(f"{num} appears {arr[num]} times in array")
    
num = 2
hash = [2, 3, 4, 3, 2, 2, 6]

print(TrueHashmap(num, hash))