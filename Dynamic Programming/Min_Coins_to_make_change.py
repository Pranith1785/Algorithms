## Problem Statement
'''
Minimum number of coins required to make change for given amount
Example : Amount = 7
          Denominations = [1,5,10]
        Ans : 3 (1- 5rupee + 2 -1rupee)
'''


## Solution 1
## Time - O(n*d) # n- amount; d- length of denominations array
## Space - O(n)
def minCoinsToMakeChange(amount,denominations):
    minCoins = [float('inf') for i in range(amount+1)]
    minCoins[0] = 0

    for coin in denominations:
        for value in range(amount+1):
            if coin <= value:
                minCoins[value] = min(minCoins[value],minCoins[value-coin]+1)
    
    return minCoins[amount] if minCoins[amount] != float('inf') else -1

amount = 135
denominations = [39, 45, 130, 40, 4, 1, 60, 75]
print(minCoinsToMakeChange(amount,denominations))
