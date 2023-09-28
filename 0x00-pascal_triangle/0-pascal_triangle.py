#!/usr/bin/python3
"""
Pascal's Triangle Technical interview Qn
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""

    if n <= 0:
        return []

    pt = []

    for x in range(1, n + 1):
        z = 1
        tempo = [1]
        for y in range(1, x):
            # using Binomial Coefficient
            z = z * (x - y) // y
            tempo.append(z)
        # tempo.append(1)
        pt.append(tempo)
        # print(p)

    return pt
