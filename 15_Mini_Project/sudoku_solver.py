"""
Project: Sudoku Solver
Description: Solves a 9x9 Sudoku puzzle using Backtracking Algorithm
"""

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, pos):
    row, col = pos

    # Check row
    for i in range(9):
        if board[row][i] == num and col != i:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and row != i:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def main():
    print("Enter Sudoku puzzle (use 0 for empty cells):")
    board = []

    for i in range(9):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        board.append(row)

    print("\nSolving Sudoku...\n")

    if solve(board):
        print(" Solution Found:\n")
        print_board(board)
    else:
        print(" No solution exists.")


if __name__ == "__main__":
    main()