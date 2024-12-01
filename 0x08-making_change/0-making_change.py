#!/usr/bin/python3

""" makeChange function"""

def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make a given total.

    Args:
        coins (list): List of coin denominations available.
        total (int): Target total amount to make.

    Returns:
        int: Minimum number of coins needed, or -1 if impossible.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
