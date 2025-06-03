def itSelf(i, n):
    if i < n:
        return
    itSelf(i - 1, n)
    print(i)

itSelf(3, 1)
