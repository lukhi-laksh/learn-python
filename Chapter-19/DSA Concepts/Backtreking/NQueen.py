def check(n: int, board: list, i: int, j: int):
    # Upper left Dignal
    row, column = i, j
    while(row>-1 and column > -1):
        if(board[row][column] == 'Q'):
            return 0
        row -= 1 
        column -= 1
        
    # Upper right Dignal
    row, column = i, j
    while(row>-1 and column < n):
        if(board[row][column] == 'Q'):
            return 0
        row -= 1
        column += 1
    return 1

def SolveNQueen(n):
    ans = []
    board = ['.' * 4 for _ in range(4)]
    column = [0] * 4
    find(0, n, ans, board, column)
    return ans
    
def find(row: int, n: int, ans: list, board: list, column: list):
    # Base Condition

    # Put Queen at any n condition
    
    for j in range(n):
        if column[j] == 0 and check(n, board, row, j):
            column[j] = 1
            board[row] = board[row][:j] + 'Q' + board[row][j+1:]
            find(row + 1, n, ans, board, column)
            column[j] = 0
            board[row] = board[row][:j] + '.' + board[row][j+1:]
    return ans
            
print(SolveNQueen(4))