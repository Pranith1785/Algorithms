
## Problem statement
'''
300. Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

'''

## Solution 1
## TIme - O(n**2)  | Space - O(n)

def longestSubSequence(nums:list[int]) -> int:

    arrLenLSS = [1] * len(nums)

    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                arrLenLSS[i] = max(arrLenLSS[i], 1+arrLenLSS[j])
    
    return max(arrLenLSS)

    

arr = [10,9,2,5,3,7,101,18]
print(longestSubSequence(arr))

