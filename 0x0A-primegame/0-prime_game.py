#!/usr/bin/python3
'''
solution for solving the prime game
'''


def is_prime(n):
    '''
    Checks if n is a prime number
    '''
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    '''
    Solves the prime game between Maria an Ben
    '''
    if x <= 0 or len(nums) == 0 or len(nums) < x:
        return None
    result = {"Maria": 0, "Ben": 0}
    for i in range(x):
        primes = []
        for j in range(1, nums[i] + 1):
            if is_prime(j):
                primes.append(j)
        if len(primes) % 2 == 0:
            result['Ben'] += 1
        else:
            result['Maria'] += 1
    if result['Maria'] > result['Ben']:
        return 'Maria'
    elif result['Maria'] < result['Ben']:
        return 'Ben'
    else:
        return None
