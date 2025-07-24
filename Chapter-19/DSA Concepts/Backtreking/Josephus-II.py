def Winner(n, k):
    
    if n == 1:
        return 0
    
    return (Winner(n - 1, k) + k) % n

n = 5
k = 2
print(Winner(n, k))