#!/usr/bin/python3
'''
a method that determines if a given data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    '''
    verify utf-8 compatibility
    '''
    data = iter(data)
    for i in data:
        no_byte = leadingOnes(i)
        if no_byte in [1, 5, 6, 7, 8]:
            return False
        for j in range(no_byte - 1):
            trail = next(data, None)
            if trail is None or trail >> 6 != 0b10:
                return False
    return True


def leadingOnes(b):
    '''
    Calculates number of bytes of character
    '''
    byte = bin(b).replace('0b', '').rjust(8, '0')
    count = 0
    byte_str = str(byte)
    if byte_str[0] == "0":
        return 0
    for i in range(8):
        if byte_str[i] == "1":
            count += 1
        else:
            return count
    return 8
