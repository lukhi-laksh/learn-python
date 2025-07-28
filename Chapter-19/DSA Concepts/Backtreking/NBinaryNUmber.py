def binN(s, i, j, ans):
    if len(s) == 4:
        ans.append(s)
        return

    binN(s + "0", i + 1, j, ans)

    if j < i:
        binN(s + "1", i, j + 1, ans)

