## Problem Statement
'''
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3. Its maximum jump length is 0, 
which makes it impossible to reach the last index.
'''

## Solution
## Time - O(n) | Space - O(1)
def canJump(nums: list[int]) -> bool:
    """
    Determines if the end of the array can be reached.
    """
    if not nums:
        return False
    
    max_reach = 0
    last_index = len(nums) - 1

    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
        if max_reach >= last_index:
            return True
            
    return True # Should be unreachable if logic is correct, but covers single-element arrays