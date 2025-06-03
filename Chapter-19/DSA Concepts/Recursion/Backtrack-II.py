def backtrack(i, n):
    if i > n:
        return
    
    backtrack(i + 1, n)
    print(i)



backtrack(1, 10)