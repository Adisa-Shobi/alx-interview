#!/usr/bin/python3
'''
a method that determines if a given data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    '''
    verify utf-8 compatibility
    '''
    for i in data:
        binary_i = decimalToBinary(i)
        no_byte = charLength(binary_i)
        if not no_byte or no_byte > 4 or len(str(binary_i)) > 8:
            return False
    return True


def decimalToBinary(n):
    '''
    Converts a decimal to binary
    '''
    return bin(n).replace("0b", "")


def charLength(b):
    '''
    Calculates number of bytes of character
    '''
    count = 0
    binary_digits = str(b)
    if binary_digits[0] == '0':
        return 1
    for char in binary_digits:
        if char == '1':
            count += 1
        elif char == '0':
            return count
    return None
