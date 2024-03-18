
### Problem Statement
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:
          Input: nums1 = [1,3], nums2 = [2]
          Output: 2.00000
          Explanation: merged array = [1,2,3] and median is 2.

Example 2:
          Input: nums1 = [1,2], nums2 = [3,4]
          Output: 2.50000
          Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''

## Solution -1
## Time  -  O(n+m)   | Space  - O(n+m)
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:

    newArray = []

    l1_idx = 0
    l2_idx = 0

    while(True):
        if l1_idx >= len(nums1):
            newArray.extend(nums2[l2_idx:])
            break
        
        if l2_idx >= len(nums2):
            newArray.extend(nums1[l1_idx:])
            break

        if nums1[l1_idx] < nums2[l2_idx]:
            newArray.append(nums1[l1_idx])
            l1_idx += 1
        else:
            newArray.append(nums2[l2_idx])
            l2_idx += 1
    
    midIdx = len(newArray)//2
    if len(newArray) % 2== 0:
        return (newArray[midIdx-1] + newArray[midIdx])/2
    else:
        return newArray[midIdx]
    

## Solution - 2
## Time -     | Space - 
## Approach : 
##     1. Get the total length and calculate median index(x)
##     2. Select list1 and get the left(l), right(r), middle index (m) and select first m values from list
##     3. Now select first (x-m)values from list2
##     4. Now check list1 (m+1) value should be less than list2(x-m) and vice-versa
##     5. If above condition fails, move the l/r index to m and calcuate middle index again
##
def findMedianSortedArrays2(nums1 : list[int], nums2 : list[int]) -> float:

    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total //2

    if len(A) > len(B):
        A , B = B, A
    l , r = 0, len(A)-1
    while True:
        
        i = (l+r) // 2  ## A
        j = half - i - 1  ## B
 
        A_left = A[i] if i >= 0 else float("-infinity")
        A_right = A[i+1] if (i+1) < len(A) else float("infinity")
        B_left = B[j] if j >= 0 else float("-infinity")
        B_right = B[j+1] if (j+1) < len(B) else float("infinity")

        if A_left <= B_right and B_left <= A_right:
            ##Odd
            if total % 2 == 1:
                return min(A_right,B_right)
            ## Even
            return (max(A_left,B_left)+ min(A_right,B_right))/2
        
        elif A_left > B_right:
            r = i -1
        else:
            l = i + 1

 

