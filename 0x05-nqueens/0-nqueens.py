#!/usr/bin/python3
"""
A module with the function: nqueens
"""
import sys


def usage():
    """invaild argv"""
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid_input(n):
    """vaild input from argv"""
    if not isinstance(n, int) or n < 4:
        return False
    return True


def is_safe(board, row, col, n):
    """chks safety of opposite queens"""
    if 0 <= row < len(board) and 0 <= col < len(board[row]):
        if board[row][col]:
            return False

    for i in range(1, n):
        if 0 <= row + i < len(board) and 0 <= col + i < len(board[row + i]):
            if board[row + i][col + i]:
                return False
        if 0 <= row - i < len(board) and 0 <= col - i < len(board[row - i]):
            if board[row - i][col - i]:
                return False
        if 0 <= row + i < len(board) and 0 <= col - i < len(board[row + i]):
            if board[row + i][col - i]:
                return False
        if 0 <= row - i < len(board) and 0 <= col + i < len(board[row - i]):
            if board[row - i][col + i]:
                return False

    return True


def solve_n_queens(board, row, n):
    """main soln"""
    if row == n:
        return [board]

    solutions = []
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solutions += solve_n_queens(board, row + 1, n)
            board[row][col] = 0

    return solutions


def print_solution(solution):
    """prints the list of lists format"""
    string = ""
    for row in solution:
        for col in row:
            string += str(col)
        string += "\n"
    print(string)


def main():
    """main entrance of the soln"""
    if len(sys.argv) != 2:
        usage()

    n = int(sys.argv[1])
    if not is_valid_input(n):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for i in range(n)] for j in range(n)]
    solutions = solve_n_queens(board, 0, n)

    for solution in solutions:
        print_solution(solution)


if __name__ == '__main__':
    main()
