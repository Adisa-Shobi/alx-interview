#!/usr/bin/python3
'''
finds the perimeter of a of an island represented by a grid
'''


def island_perimeter(grid):
    '''
    Returns the perimeter of the island described in grid
    '''
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                result += check_surrounding(i, j, grid)
    return result


def check_surrounding(i, j, grid):
    '''
    Checks all surrounding cells for perimeter
    '''
    height = len(grid) - 1
    width = len(grid[0]) - 1
    perimeter = 0

    if i == 0 or not grid[i-1][j]:
        perimeter += 1
    if j == 0 or not grid[i][j-1]:
        perimeter += 1
    if i == height or not grid[i+1][j]:
        perimeter += 1
    if j == width or not grid[i][j+1]:
        perimeter += 1
    return perimeter
