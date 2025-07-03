def laksh(n):
    if n == 1 or n == 0:
        return n
    
    return laksh(n - 1) + laksh(n - 2)

print(laksh(5))