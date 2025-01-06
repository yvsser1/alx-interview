#!/usr/bin/python3
"""Module for calculating minimum number of operations to reach n H characters"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve exactly n H characters.

    Args:
        n (int): Target number of H characters to achieve

    Returns:
        int: Minimum number of operations (Copy All + Paste) needed.
             Returns 0 if n is impossible to achieve.

    The approach uses prime factorization since the optimal solution follows
    the pattern of multiplying numbers to reach n. Each prime factor contributes
    its value to the total number of operations needed.
    """
    # If n is 1 or less, we need 0 operations
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Perform prime factorization and sum the factors
    while n > 1:
        while n % divisor == 0:
            # Each prime factor represents a Copy All + Paste sequence
            operations += divisor
            n //= divisor
        divisor += 1

        # Optimization: If divisor squared is greater than n,
        # and n is not 1, then n is prime
        if divisor * divisor > n and n > 1:
            operations += n
            break

    return operations
