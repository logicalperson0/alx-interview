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
                # chk top and if x = 0 then it is water beyond grid-top
                if grid[x - 1][y] == 0 or x == 0:
                    z += 1
                # chk left and if y = 0 then it is water beyond grid-left
                if grid[x][y - 1] == 0 or y == 0:
                    z += 1
                # chk bottom and if x = grid-len then
                # it is water beyond grid-bottom
                if x == (len(grid) - 1) or grid[x + 1][y] == 0:
                    z += 1
                # chk right and if y = grid-row-len then
                # it is water beyond grid-right
                if y == (len(grid[0]) - 1) or grid[x][y + 1] == 0:
                    z += 1

    return (z)
