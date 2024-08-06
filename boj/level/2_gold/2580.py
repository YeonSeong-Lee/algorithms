import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]


def is_valid(board, row, col, num):
    # 가로줄 검사
    if num in board[row]:
        return False
    # 세로줄 검사
    if num in [board[i][col] for i in range(9)]:
        return False
    # 3x3 박스 검사
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return False
    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


solve_sudoku(board)

for e in board:
    print(*e)
