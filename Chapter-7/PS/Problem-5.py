l = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0

while i < len(l):
    if(l[i] == x):
        print("Found at index", i)
        break
    else:
        print("find more...")
    i += 1