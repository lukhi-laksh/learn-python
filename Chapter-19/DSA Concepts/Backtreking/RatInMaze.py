def Total(arr: list, i: int, j: int, n: int, path: list, ans: list, visited: list):
    if (i == n - 1) and (j == n - 1):
        ans.append("".join(path))
        return

    row = [-1, 1, 0, 0]
    col = [0, 0, -1, 1]
    dir = "UDLR"


    visited[i][j] = 1
    for k in range(4):
        if (valid(i + row[k], (j + col[k]), n)) and (arr[i + row[k]][j + col[k]]) and not(visited[i + row[k]][j + col[k]]):
            path.append(dir[k])
            Total(arr, i + row[k], j + col[k], n, path, ans, visited)
            path.pop()
    


