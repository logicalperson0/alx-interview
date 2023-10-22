#!/usr/bin/python3
"""
A module with a fun: minOperations
"""


def minOperations(n):
    """method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file"""
    chars_pro = 2
    opers = 0

    if n < 1:
        return 0

    while n > 1:
        while (n % chars_pro == 0):
            n /= chars_pro
            opers += chars_pro
        chars_pro += 1

    return opers
