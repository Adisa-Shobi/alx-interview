#!/usr/bin/env python3
'''
N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard
'''
import sys
from typing import List


results = []
def solve_n_queens(n):
    '''
    Driver code for util function
    '''
    results.clear()
    board = [[0] * n for i in range(n)]
    solve_n_util(board, 0)
    results.sort()
    return results


def is_safe(board: List[List[int]], row: int, col: int):
    '''
    checks if position is safe for queen
    '''
    for i in range(col):
        if board[row][i]:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while j >= 0 and i < len(board):
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve_n_util(board, col):
    '''
    Solves n queens using backtracking
    '''
    print(col)
    size = len(board)
    if col == size - 1:
        sub = []
        for i in range(size):
            for j in range(size):
                if board[i][j] == 1:
                    sub.append([i, j])
        results.append(sub)
        return True

    res = False
    for i in range(size):
        if (is_safe(board, i, col)):
            board[i][col] = 1

            res = solve_n_util(board, col + 1) or res

            board[i][col] = 0

    return res

arg_len = len(sys.argv)
if arg_len != 2:
    print("Usage: nqueens N")
    exit(1)
else:
    board_size = int(sys.argv[1])
    res = solve_n_queens(board_size)
    print(res)
