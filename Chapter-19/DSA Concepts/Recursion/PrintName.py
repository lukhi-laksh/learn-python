def printName(i, n):
    if i > n:
        return
    print("laksh lukhi")
    printName(i + 1, n)
    
printName(1, 5)