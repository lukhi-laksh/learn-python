def printing(n):
    if (n == 1):
        return print(1)
    
    print(n)
    printing(n - 1)

printing(3)