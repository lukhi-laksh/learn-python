def laksh(s, n):
    if n == -1:
        return s
    
    l = chr(ord(s[n]) - 32)
    s[n] = l

    return laksh(s, n - 1)

n = list("harsh")
p = len(n) - 1
sure = (laksh(n, p))
print("".join(sure)) 