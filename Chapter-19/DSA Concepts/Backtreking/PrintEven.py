def recur(n):
    if n == 0:
        return
    print(n)
    recur(n - 2)

recur(18)