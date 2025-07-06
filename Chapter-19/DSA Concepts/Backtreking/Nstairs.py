def laksh(n):
    # Base case
    if n == 1 or n == 0:
        return n

    # Function Recall
    return laksh(n - 1) + laksh(n - 2)

print(laksh(5))
