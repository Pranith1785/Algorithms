
## Problem Statement
'''
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting? 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

'''

## Solution 1
## Time - O(n+nlog(n)) | Space - O(1)

import heapq
def kthLargest1(nums, k):

    nums.sort()

    return nums[len(nums)-k]


## Solution 2
## Time  -   | Space - 

def kthLargest2(nums,k):

    k = len(nums)-k

    def quickSelect(l,r):
        left , pivotVal= l, nums[r]

        for i in range(l,r):
            if nums[i] <= pivotVal:
                nums[left],nums[i] = nums[i], nums[left]
                left += 1
        nums[left], nums[r]  = nums[r],nums[left]


        if left > k :
            return quickSelect(l,left-1)
        elif left < k :
            return quickSelect(left+1,r)
        else:
            return nums[left]
    
    
    return(quickSelect(0,len(nums)-1))


## Solution 3
## Time - O(nlogk) | space - O(k)
import heapq
def kthLargest3(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return min_heap[0]

nums = [3,6,1,5,2,4]
k = 2

print(kthLargest3(nums,k))
