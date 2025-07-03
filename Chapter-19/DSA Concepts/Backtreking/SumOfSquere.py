def laksh(n):
    if n == 1:
        return 1
    
    return ((n * n) + laksh(n - 1))

print(laksh(5))
