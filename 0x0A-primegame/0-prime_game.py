#!/usr/bin/python3
"""Prime Game Interview QN TYPE"""


def isWinner(x, nums):
    """Maria and Ben are playing a game
    Result: Ben has the most wins"""
    # benwins = 0
    # mariawins = 0

    sieve = [True] * (max(nums) + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max(nums)**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max(nums) + 1, i):
                sieve[j] = False

    # Count the number of primes remaining after each round
    primes_remaining = [sum(sieve[i] for i in nums)]
    for _ in range(x - 1):
        # Remove multiples of the chosen prime from the sieve
        prime = max(i for i in range(2, max(nums) + 1)
                    if sieve[i] and i in nums)
        for j in range(prime * prime, max(nums) + 1, prime):
            sieve[j] = False
        primes_remaining.append(sum(sieve[i] for i in nums))

    # Determine the winner based on the parity of the
    # number of primes remaining
    if sum(primes_remaining[::2]) % 2 == 0:
        return "Winner: Maria"
    else:
        return "Winner: Ben"
