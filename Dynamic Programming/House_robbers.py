### Problem statement
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

'''

### Solution 1
## Time - O(n)  | Space - O(1)

def house_robbers(nums : list) -> int:

    if len(nums) == 0:
        return 0
    if len(nums) <= 2:
        return max(nums)
    
    first = nums[0]
    second = max(nums[0],nums[1])
    for i in range(2,len(nums)):
        currSum = max(second,nums[i] + first)
        first = second
        second = currSum

    return second


house_amounts = [5,2,6,9,3,1]
print(house_robbers(house_amounts))


