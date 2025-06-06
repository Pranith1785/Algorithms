## Problem Statement
'''
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

'''

## Solution -1
## Time - O(n)  | Space - O(n)
def majorityElement(nums:list[int]) -> int:

    numsCountMap = {}
    majority = len(nums)//2
    print(majority)
    for num in nums:
        if num in numsCountMap:
            numsCountMap[num] += 1
        else:
            numsCountMap[num] = 1
        if numsCountMap[num] > majority:
            return num 
    
    return -1


## Solution 2
## Time - O(nlogn) | Space - O(1)
def majorityElement2(nums):
    nums.sort()
    return nums[len(nums)//2]


list1 = [1]
print(majorityElement2(list1))