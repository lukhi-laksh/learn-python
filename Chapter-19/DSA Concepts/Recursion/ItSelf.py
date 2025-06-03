def itSelf(i):
    if i == 5:
        return
    print(i)
    itSelf(i + 1)

itSelf(1)
