def TrueHashmap(num, hash):
    arr = [0] * 7
    for i in range(len(hash)):
        arr[hash[i]] += 1 
    return arr[num]
        

num = 6
hash = [2, 3, 4, 3, 2, 2, 6]

print(TrueHashmap(num, hash))