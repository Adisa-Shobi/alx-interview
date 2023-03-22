#!/usr/bin/python3
'''
a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total
'''


def makeChange(coins, total):
    '''
    makes change for total
    '''
    coins = sorted(coins)[::-1]
    if total <= 0:
        return 0
    return get_largest(0, total, coins)


def get_largest(no_coins, remainder, coins):
    '''Eliminates the largest coin
    '''
    if remainder == 0:
        return no_coins
    for coin in coins:
        if coin > remainder:
            coins.remove(coin)
            return get_largest(no_coins, remainder, coins)
        elif coin == remainder:
            return no_coins + 1
        else:
            coins.remove(coin)
            return get_largest(
                no_coins + (remainder // coin),
                remainder % coin,
                coins
            )
    if remainder > 0:
        return -1
