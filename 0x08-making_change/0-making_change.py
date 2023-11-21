#!/usr/bin/python3


def makeChange(coins, total):
    """return: the fewest number of coins needed to meet a
    given amount total"""
    if total <= 0:
        return 0
    coins.sort()
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
