def laksh(a, b):
    # Base case
    if b == 0:
        print(a)
        return

    laksh(b, a % b)

laksh(150, 200)
