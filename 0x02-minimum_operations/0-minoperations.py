#!/usr/bin/python3
'''
minimum operations solution algorithm
'''
from math import floor


def minOperations(n, ops=0):
    '''
    number of operations required to get n Hs
    '''
#    ops = 0
#    clipboard = 2
#    while n > 1:
#        while n % clipboard == 0:
#            ops += clipboard
#            n = n / clipboard
#        clipboard += 1
#    return ops
    for i in range(2, (n // 2) + 1)[::-1]:
        if n % i == 0:
            return minOperations(i, ops + (n / i))
    return int(ops + n)
