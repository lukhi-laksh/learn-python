def sums(n):
    if (n == 0):
        print("Happy Birthday")
        return
    print(n, "days left for birthday")
    sums(n - 1)

sums(10)