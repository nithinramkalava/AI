import numpy as np


def printSolution(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))


def isSafe(board, row, col):
    # its row
    if any(board[row, :col]):
        return False

    # diagonal 1
    if any(board[i, j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        return False

    # diagonal 2
    if any(board[i, j] for i, j in zip(range(row, N), range(col, -1, -1))):
        return False

    return True


def solveNQUtil(board, col):
    if col >= N:
        return True

    for row in range(N):
        if isSafe(board, row, col):
            board[row, col] = 1
            if solveNQUtil(board, col + 1):
                return True
            board[row, col] = 0

    return False


def solveNQ():
    board = np.zeros((N, N), dtype=int)
    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


N = int(input("Enter number of queens: "))
solveNQ()
