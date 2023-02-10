#!/usr/bin/python3
'''
minimum operations solution algorithm
'''
from math import floor


def minOperations(n, ops=0):
    '''
    number of operations required to get n Hs
    '''
    if (n <= 1):
        return 0
    for i in range(2, (n // 2) + 1)[::-1]:
        if n % i == 0:
            return minOperations(i, ops + (n / i))
    return int(ops + n)
