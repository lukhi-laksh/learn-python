def funs(n):
    if n == 0:
        return 0

    return n + funs(n - 1)
    

print(funs(7))