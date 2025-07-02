def laksh(n, A):
    if n == A:
        return print(n)
        
    print(n)
    laksh(n + 1, A)

laksh(1, 7)