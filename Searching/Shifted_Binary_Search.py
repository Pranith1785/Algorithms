### Problem
'''
Find the index of a given integer in shifted sorted array of length n.
If exists return index position or else -1
'''

### Solution 1
# Time  - O(log(n))
# Space  - O(log(n))
def shiftedBinarySearch(array,target):
    return shiftedBinarySearchHelper(array,0,len(array)-1,target)

def shiftedBinarySearchHelper(array, leftIdx,rightIdx,target):
    if leftIdx > rightIdx :
        return -1
    middleIdx = (leftIdx + rightIdx) // 2
    leftValue = array[leftIdx]
    rightValue = array[rightIdx]
    middleValue = array[middleIdx]

    if middleValue == target:
        return middleIdx
    elif leftValue <= middleValue :
        if target < middleValue and target >= leftValue:
            return shiftedBinarySearchHelper(array,leftIdx,middleIdx-1,target)
        else:
            return shiftedBinarySearchHelper(array,middleIdx+1,rightIdx,target)
    else:
        if target > middleValue and target <= rightValue:
            return shiftedBinarySearchHelper(array,middleIdx+1,rightIdx,target)
        else:
            return shiftedBinarySearchHelper(array,leftIdx,middleIdx-1,target)



#### Solution 2
# Time - O(log(n)) | Space - O(1)
def shiftedBinarySearch1(array,target):
    leftIdx = 0
    rightIdx = len(array)-1

    while leftIdx <= rightIdx:
        middleIdx = (leftIdx + rightIdx) // 2
        leftValue = array[leftIdx]
        rightValue = array[rightIdx]
        middleValue = array[middleIdx]

        if middleValue == target:
            return middleIdx
        elif leftValue <= middleValue :
            if target < middleValue and target >= leftValue:
                rightIdx = middleIdx-1
            else:
                leftIdx = middleIdx + 1
        else:
            if target > middleValue and target <= rightValue:
                leftIdx = middleIdx + 1
            else:
                rightIdx = middleIdx -1
    return -1


arr = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
findVal = 37

print(shiftedBinarySearch1(arr,findVal))