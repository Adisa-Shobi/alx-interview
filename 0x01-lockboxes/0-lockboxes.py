#!/usr/bin/python3
'''
Solution to lockbox challenge
'''


def canUnlockAll(boxes):
    '''
    Function loops through all lockboxes opening each once the key is found
    '''
    open_boxes = [False] * len(boxes)
    open_boxes[0] = True
    for box_no, box in enumerate(boxes):
        for key_no in box:
            if key_no < len(boxes) and key_no != box_no \
               and not open_boxes[key_no]:
                open_boxes[key_no] = True
    return all(open_boxes)
