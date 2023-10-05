#!/usr/bin/python3
"""
Lockboxes Technical interview Qn
"""


def canUnlockAll(boxes):
    """ a method that determines if all the boxes can be opened for a:
    n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes"""
    if (len(boxes) == 0):
        return False

    keys = [0]

    for x in keys:
        for y in boxes[x]:
            if (y not in keys and len(boxes) > y):
                keys.append(y)
    if len(keys) == len(boxes):
        return True
    return False