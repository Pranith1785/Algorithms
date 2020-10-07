
### Problem Statement
'''
Find the number of ways to make change using the currency denominations and Amount value
Input : denomination Array = [1,5]
        Total = 6
Ouptut : 2 ways
'''

'''
Approach : 1. Create a array(ways) of length equals to total+1 and value as 0
           2. Consider each index as amount ; and value at index is "no. of ways to change the amount"
           3. Update the zeroth amount change ways to 1
           4. if each denomination is less than or equal to amount then update the 'ways' array 
           5. ways[amount(index)] = ways[amount(index)] + ways[amount-denomination]
'''

### Solution 1
## Time - O(n*d) ## n- amount ; d - denominations array length
## Space - O(n)
def currencyChange(total,denominations):

    ways = [0 for _ in range(total+1)]
    ways[0] = 1  ## no of ways to change the amount 0 is 1
    for coinValue in denominations:
        for amount in range(1,total+1):
            if amount >= coinValue:
                ways[amount] += ways[amount-coinValue]
    return ways[total]



total = 12
currDenom  = [1,2,5,10]
print(currencyChange(total,currDenom))