def laksh(s, f, l):
    
    if f >= l:
        return s
    
    s[f], s[l] = s[l], s[f]

    return laksh(s, f + 1, l - 1)

n = list("laksh")
p = len(n) - 1
sure = (laksh(n, 0, p))
print("".join(sure)) 