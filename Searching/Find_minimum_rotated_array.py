
## Problem Statement
'''
153. Find Minimum in Rotated Sorted Array

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time. 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

'''

## Solution 1
## Time - O(nlogn)  | Space - O(1)

def findMin(nums):
    leftIdx , rightIdx = 0, len(nums)-1
    
    minValue = nums[0]

    while(leftIdx <= rightIdx):
        if nums[leftIdx] < nums[rightIdx]:
            minValue = min(minValue, nums[leftIdx])
            break
        
        midIdx = (leftIdx+rightIdx)//2
        minValue = min(minValue, nums[midIdx])

        if nums[midIdx] >= nums[leftIdx]:
            leftIdx = midIdx + 1
        else:
            rightIdx = midIdx - 1
    
    return minValue


print(findMin([9,1,3,5,7]))
