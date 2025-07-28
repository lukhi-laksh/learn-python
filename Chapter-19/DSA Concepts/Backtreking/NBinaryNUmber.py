def binN(s, i, j, ans):
    if len(s) == 4:
        ans.append(s)
        return

    if j < i:
        binN(s + "1", i, j + 1, ans)
    
    
    binN(s + "0", i + 1, j, ans)


s = ""
i = 0
j = 0
ans = []
binN(s, i, j, ans)
print(ans)

# output:- ['0101', '0100', '0011', '0010', '0001', '0000']
