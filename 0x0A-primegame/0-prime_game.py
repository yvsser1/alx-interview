#!/usr/bin/python3
"""Prime Game - Maria and Ben are playing a game"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def play_round(n):
    """
    Play a single round of the prime game.
    Returns True if Maria wins, False if Ben wins.
    """
    # Create the initial set of numbers
    numbers = set(range(1, n + 1))
    
    # Track the current player (True for Maria, False for Ben)
    maria_turn = True
    
    while True:
        # Find available prime numbers in the current set
        available_primes = [p for p in range(2, n + 1) if p in numbers and is_prime(p)]
        
        # If no primes are available, current player loses
        if not available_primes:
            return not maria_turn
        
        # Choose the smallest prime
        prime_choice = min(available_primes)
        
        # Remove the chosen prime and its multiples
        numbers = {num for num in numbers if num % prime_choice != 0}
        
        # Switch turns
        maria_turn = not maria_turn

def isWinner(x, nums):
    """
    Determine the overall winner across x rounds.
    
    Args:
    x (int): Number of rounds
    nums (list): List of n values for each round
    
    Returns:
    str or None: Winner of most rounds ('Maria', 'Ben', or None)
    """
    # Validate input
    if x != len(nums):
        return None
    
    # Track wins
    maria_wins = 0
    ben_wins = 0
    
    # Play each round
    for n in nums:
        if play_round(n):
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
