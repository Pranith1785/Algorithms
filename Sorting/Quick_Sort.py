### Problem Statement
'''
Sort the given integers in an array of size "n"

Approach : 
1. pick any element as pivot point (start, last or any)
2. picked last element as pivot
3. create a partition by moving all elements less than pivot to left and greater values to right
4. Repeat the same for the left and right partitions 
'''

## Solution
# Time - O(nlog(n))
# Space - O(log(n))
def quickSorthelper(array,left,right):
    pivot = array[right]

    for i in range(left,right):
        if array[i] < pivot :
            array[left],array[i] = array[i],array[left]
            left += 1
    array[left],array[right] = array[right],array[left]
    return left

def quickSort(array,left,right):
    if left < right :
        pos = quickSorthelper(array,left,right)
        ## apply quick sort for partitions of left and right
        quickSort(array,left,pos-1)
        quickSort(array,pos+1,right)

    return array


arr = [8, 5, 2, 9, 5, 6, 3]
print(quickSort(arr,0,len(arr)-1))