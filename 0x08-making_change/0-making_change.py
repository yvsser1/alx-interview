def makeChange(coins, total):
    # Handle base cases
    if total < 0:
        return -1
    if total == 0:
        return 0
    
    # Initialize DP array with a large value (total+1 is effectively infinity)
    # We'll use total+1 as our "impossible" marker
    dp = [total+1] * (total+1)
    dp[0] = 0  # 0 coins needed to make 0
    
    # Build solution bottom-up
    for amount in range(1, total+1):
        for coin in coins:
            # Check if current coin can be used
            if coin <= amount:
                # Update minimum number of coins 
                dp[amount] = min(dp[amount], dp[amount-coin] + 1)
    
    # Return result, converting to -1 if no solution found
    return dp[total] if dp[total] <= total else -1
