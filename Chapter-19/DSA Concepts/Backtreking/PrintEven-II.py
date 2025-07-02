def laksh(n):
    if n == 0:
        return
    laksh(n - 2)
    print(n)

laksh(10)