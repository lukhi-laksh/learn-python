def Fectorial(n):
    if n == 0:
        return 1
    return n * Fectorial(n - 1)
    
print(Fectorial(17))