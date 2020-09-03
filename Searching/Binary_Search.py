### Problem
'''
Find the index of a given integer in sorted array of length n.
If exists return index position or else -1
'''

### Solution 1
# Time  - O(logn)
# Space  - O(1)
def binarySearch(array,target):
    left = 0
    right = len(array) -1
    
    while (left <= right):
        mid = (left + right)//2 
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid -1
        else:
            left = mid +1
    
    return -1


### Solution 2
# time - O(log(n))
# space - O(log(n))
def binarySearch2(array,target):
    return binaryHelperFunction(array,target,0,len(array)-1)

def binaryHelperFunction(arr,findVal,left,right):
    if left > right:
        return -1
    mid = (left + right)//2
    midValue = arr[mid]

    if midValue == findVal:
        return mid
    elif midValue > findVal :
        return binaryHelperFunction(arr,findVal,left,mid-1)
    else:
        return binaryHelperFunction(arr,findVal,mid+1,right)


arr = [-23,-10,1,2,20,80,100,300,1000]
findVal = -21

print(binarySearch2(arr,findVal))