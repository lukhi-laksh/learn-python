def printName(n, i):
    if n < i:
        return
    print(n)
    printName(n - 1, i)
    
printName(10, 1)