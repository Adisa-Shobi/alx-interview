#!/usr/bin/python3
'''
a method that determines if a given data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    '''
    verify utf-8 compatibility
    '''
    for i in data:
        if i >= 128:
            return False
    return True
