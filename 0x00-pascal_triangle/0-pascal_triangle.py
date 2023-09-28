#!/usr/bin/python3
"""
Pascal's Triangle Technical interview Qn
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal\’s triangle of n"""

    if n <= 0:
        return []
    
    p = [0]
    
    for x in range(1, n + 1):
        c = 1
        for y in range(1, x + 1):
            c = c * (x - y) // y
            p[y] = c
    
    return p