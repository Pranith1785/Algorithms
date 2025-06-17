
## Problem statement
'''
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

'''

## Solution 1
## Time - O(n*2) | Space - O(1)

def max_product(nums):
    max_product = float("-inf")

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i==j:
                currProduct = nums[j] 
            else:
                currProduct *= nums[j]
            
            max_product = max(max_product, currProduct)

    return max_product

## Solution 2
## Time - O(N)   | Space - O(1)

def max_product2(nums):

    if not nums:
        return 0
    
    max_product = float("-inf")

    curr_product = 1
    for i in range(len(nums)):
        
        curr_product *= nums[i]
        max_product = max(max_product,curr_product)

        if curr_product == 0:
            curr_product = 1
        
    curr_product = 1
    for i in range(len(nums)-1,-1,-1):

        curr_product *= nums[i]
        max_product = max(max_product, curr_product)
        if curr_product == 0:
            curr_product = 1
    
    return max_product



print(max_product([2,3,-2,4]))