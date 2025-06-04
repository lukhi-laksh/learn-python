def para(n, sum):
    if n < 1:
        print(sum)
        return
    return para(n - 1, sum + n)


para(6, 0)