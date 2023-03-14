#!/usr/bin/python3
'''
Rotates a 2d matrix clockwise
'''


def transpose(matrix):
    '''transposes a matrix
    '''
    matrix_size = len(matrix)
    for i in range(matrix_size):
        begin_switch = False
        for j in range(matrix_size):
            if j > i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def rotate_2d_matrix(matrix):
    ''' rotate it 90 degrees clockwise.
    '''
    transpose(matrix)
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
