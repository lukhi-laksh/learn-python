def laksh(a, b):
    if b == 0:
        print(a)
        return

    laksh(b, a % b)

laksh(150, 200)