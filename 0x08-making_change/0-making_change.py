#!/usr/bin/python3
"""
Making changes
"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if (total <= 0):
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    nums = 0

    for x in coins:
        while nums < total:
            nums += x
            num_coins += 1
        if nums == total:
            return num_coins
        nums -= x
        num_coins -= 1
    return -1

# coins.sort()
    """
    i = -1
    num_coins = 0
    nums = 0

    while 1:
        nums += coins[i]
        num_coins += 1
        if nums > total:
            nums -= coins[i]
            num_coins -= 1
            i -= 1
        elif nums == total:
            return num_coins
        elif nums < total:
            if ((nums + coins[i]) > total):
                i -= 1
            if coins[i] == coins[0]:

                while 1:
                    nums += coins[0]
                    num_coins += 1
                    if nums > total:
                        return -1
                    elif nums == total:
                        return num_coins
      """
