def SolveNQueen(n):
    ans = []
    board = ['.' * 4 for _ in range(4)]
    column = [0] * 4
    rightDig = [0] * (2 * n - 1)
    leftDig = [0] * (2 * n - 1)
    find(0, n, ans, board, column, leftDig, rightDig)
    return ans
    
def find(row: int, n: int, ans: list, board: list, column: list, leftDig: list, rightDig: list):
    # Base Condition
    if row == n:
        ans.append(board[:])
    
    # Put Queen at any n possition
    
    # left Dignal: n - 1 + col-row
    # right Dignal: row + col
    
    # Put Queen at any n condition
    for j in range(n):
        if column[j] == 0 and leftDig[n - 1 + j - row] == 0 and rightDig[row + j] == 0:
            column[j] = 1
            leftDig[(n - 1) + j - row] == 1
            rightDig[row + j] == 1
            board[row] = board[row][:j] + 'Q' + board[row][j+1:]
            find(row + 1, n, ans, board, column, leftDig, rightDig)
            column[j] = 0
            leftDig[(n - 1) + j - row] == 0
            rightDig[row + j] == 0
            board[row] = board[row][:j] + '.' + board[row][j+1:]
    return ans
            
print(SolveNQueen(4))