
### Problem Statement
'''
496. Next Greater Element I

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
'''


## Solution 1
## Time - O(m*n)   | Space - O(m) 


def NextGreaterElement(nums1, nums2)-> list:

    result = [-1] * len(nums1)

    for i in range(len(nums1)):
        checkEle = False
        for j in range(len(nums2)):

            if nums2[j] > nums1[i] and checkEle:
                result[i] = nums2[j]
                break

            if nums1[i] == nums2[j]:
                print(nums1[i])
                print(j)
                checkEle = True
    
    return result



## Solution 2
## time  - O(m+n)  | Space - O(m)

def nextGreaterElement2(nums1, nums2):

    nums1Idx = { ele:idx  for idx, ele in enumerate(nums1)}
    result = [-1] * len(nums1)

    stackList = []
    for i in range(len(nums2)):
        curVal = nums2[i]
        while stackList and curVal > stackList[-1]:
            val = stackList.pop()
            idx = nums1Idx[val]
            result[idx] = curVal
            
        if  curVal in nums1:
            stackList.append(curVal)
    
    return result


nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(nextGreaterElement2(nums1, nums2))
