### Problem Statement
'''
Given a array of positive integer representing the values of coins.
Find the minimum amount(sum) of change that can't be created from given coins
Ex : coins = [1,2,5]
     Ans : 4 (which can't be created)
'''

## Solution 1
## Time - O(nlogn + n) = O(nlogn)
## Space - O(1)
def nonConstructibleChange(coins):

    coins.sort()
    currentChange = 0
    for eachCoin in coins:
        if eachCoin > currentChange + 1:
            return currentChange+1

        currentChange += eachCoin
    
    return currentChange + 1

coinsArray = [1, 1, 2, 3]
print(nonConstructibleChange(coinsArray))