def laksh(A, n):
    if n == 1:
        return 1
    
    return n * laksh(A, n - 1)

print(laksh(3, 6))