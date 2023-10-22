#!/usr/bin/python3
"""
A module with a fun: minOperations
"""


def minOperations(n):
    """method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file"""
    if n == 1:
        return 0
    elif (n % 2 == 0):
        return minOperations(n // 2) + 1
    else:
        return minOperations(n // 2 + 1) + 2