### Problem Statement
'''
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

*   For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, `[3,2,1]`.

The next permutation of an array of integers is the next lexicographically greater permutation of its integers. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such an arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

*   For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
*   Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
*   While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, find the next permutation of `nums`.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
*   `1 <= nums.length <= 100`
*   `0 <= nums[i] <= 100`

'''

## Solution 1
## Time - O(n) | Space - O(1)
def nextPermutation(nums):

    length = len(nums)

    ## Find pivot
    i = length -2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    ## Find next smallest element after the i+1 indices and which is larger than pivot value
    if i >= 0:
        j = length-1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        
        ## Swap the values
        nums[i], nums[j] = nums[j], nums[i]


    ## Reverse the sub array to right of pivot
    print(i,j)
    left , right = i+1, length-1
    print(nums)
    while left< right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


print(nextPermutation([5,4,7,5,3,2]))

## Solution 2
## Time - O(nlogn) | Space - O(1)
def nextPermutation2(nums):

    length = len(nums)

    ## Find pivot
    i = length -2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    ## Find next smallest element after the i+1 indices and which is larger than pivot value
    if i >= 0:
        j = length-1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        
        ## Swap the values
        nums[i], nums[j] = nums[j], nums[i]


    ## Sort the sub array to right of pivot
    nums[i+1:] = sorted(nums[i+1:])

    return nums

