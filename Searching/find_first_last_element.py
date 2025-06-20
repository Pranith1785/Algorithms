### Problem Statement
'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

'''

# Solution 1
# Time Complexity: O(log n) | Space Complexity: O(1)
def searchRange(nums, target):

    def findLeft(nums,target):
        left, right = 0, len(nums)-1
        leftidx = -1
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] == target:
                leftidx = mid
                right = mid-1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid +1
            
            if right == left:
                if nums[left] == target:
                    leftidx =left
                break

        return leftidx
    
    def findRight(nums,target):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)-1
        rightIdx = -1
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] == target:
                rightIdx = mid
                left = mid+1
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid +1
            
            if right == left:
                if nums[left] == target:
                    rightIdx =left
                break

        return rightIdx

        
    left = findLeft(nums,target)
    right = findRight(nums,target)

    return [left,right]


print(searchRange( [1],1))

