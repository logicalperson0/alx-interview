#!/usr/bin/python3
"""Prime Game Interview QN TYPE"""


def isWinner(x, nums):
    """Maria and Ben are playing a game
    Result: Ben has the most wins"""
    wins_ben = 0
    wins_maria = 0
    n = len(nums)

    for _ in range(x):
        # First move for Maria
        if n == 1:
            wins_maria += 1
            continue

        # Find a suitable prime for Maria if possible
        prime_found = False
        for num in nums:
            if is_prime(num) and (n - len(get_multiples(num, n))) > (n // 2):
                nums = [i for i in nums if i % num != 0]
                n = len(nums)
                prime_found = True
                break

        # Check if Maria won after her move
        if n == 0:
            wins_maria += 1
            continue

        # Check if Ben can win with a single move after Maria's move
        if n > 2 and (nums[0] % 2 == 0 and get_common_diff(nums) % 2 == 0):
            wins_ben += 1
            continue

        # If no definite winner yet, Maria loses after ben's move
        wins_ben += 1

    if wins_maria > wins_ben:
        return "Maria"
    else:
        if wins_ben > wins_maria:
            return "Ben"
        else:
            return None


def is_prime(num):
    """
    Checks if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_multiples(num, n):
    """
    Gets all multiples of a number within a range.
    """
    return [i for i in range(1, n + 1) if i % num == 0]


def get_common_diff(nums):
    """
    Gets the common difference of a sorted sequence.
    """
    if len(nums) < 2:
        return None
    return nums[1] - nums[0]
