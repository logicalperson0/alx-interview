#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    z = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (grid[x][y]) == 1:
                # z += 4
                if grid[x - 1][y] == 0 or x == 0:
                    z += 1
                if grid[x][y - 1] == 0 or y == 0:
                    z += 1
                if x == (len(grid) - 1) or grid[x + 1][y] == 0:
                    z += 1
                if y == (len(grid[0]) - 1) or grid[x][y + 1] == 0:
                    z += 1
                
    return (z)