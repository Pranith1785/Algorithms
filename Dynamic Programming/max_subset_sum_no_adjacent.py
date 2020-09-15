### Problem Statement
'''
Function which gives the max sum of non-adjacent elements in a array
Approach :
 maxSub[i] = maxSub[i-1] or max(maxSub[i-2],arr[i])
'''

### Solution 1
## Time - O(n)
## Space - O(n)
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    if len(array) == 1:
        return array[0]
    max_Subset = [array[0],max(array[0],array[1])]
    for i in range(2,len(array)):
        maxSum = max(max_Subset[i-1],array[i] + max_Subset[i-2])
        max_Subset.append(maxSum)
    
    return max_Subset[-1]


### Solution 2
## Time - O(n)
## Space - O(1)
def maxSubsetSumNoAdjacent1(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    first = array[0]
    second = max(array[0],array[1])
    for i in range(2,len(array)):
        current = max(second,first + array[i])
        first = second
        second = current
    
    return second


arr = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent1(arr))