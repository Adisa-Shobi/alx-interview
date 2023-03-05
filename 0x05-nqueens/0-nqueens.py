#!/usr/bin/python3
"""
N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard
"""
import sys

results = []


def add_solution(board):
    """Adds completed solution to results
    """
    length = len(board)
    sub = []
    for i in range(length):
        for j in range(length):
            if board[i][j] == "Q":
                sub.append([i, j])
    results.append(sub)


def nqueens(n):
    """Backtracking to find solutions to N queens
    """
    # Create an empty board
    board = [['.' for i in range(n)] for j in range(n)]
    # Define helper functions

    def is_valid(row, col):
        """checks if position is safe to place queen
        """
        for i in range(n):
            if board[i][col] == 'Q':
                return False
            if row-i >= 0 and col-i >= 0 and board[row-i][col-i] == 'Q':
                return False
            if row-i >= 0 and col+i < n and board[row-i][col+i] == 'Q':
                return False
        return True

    def backtrack(row):
        """Locates plausible solutions
        """
        if row == n:
            # Found a solution, print it
            add_solution(board)
            return
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    # Start the search
    backtrack(0)


# Parse the command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Solve the problem
nqueens(n)
for soln in results:
    print(soln)
