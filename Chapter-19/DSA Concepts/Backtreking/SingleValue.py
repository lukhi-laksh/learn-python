def laksh(n):
    if n == 0:
        return

    laksh(n - 1)
    print(n)
    
laksh(6)