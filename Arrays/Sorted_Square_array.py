### Problem Statement
'''
Function that takes sorted array and return square of original letters that to in sorted order
here sorted in ascending order

Example : array = [1,2,3,4,5]
          squareArray = [1,4,9,16,25]

'''

### Solution 1
## Time - O(nlog(n))   | Space - O(n) 

def sortedSquareArray(array):

    squareArray = [ele*ele for ele in array]
    squareArray.sort()
    return squareArray


### Solution 2
## Time - O(n)  | Space - O(n) 

def sortedSquareArray2(array):

    leftIdx = 0
    rightIdx = len(array)-1
    squareArray = [0 for _ in array]

    for idx in reversed(range(len(array))):
        smallerValue = array[leftIdx]
        largerValue = array[rightIdx]

        if abs(smallerValue) > abs(largerValue):
            squareArray[idx] = smallerValue*smallerValue
            leftIdx += 1
        else:
            squareArray[idx] = largerValue * largerValue
            rightIdx -= 1
    
    return squareArray



print(sortedSquareArray2([-2,1,4,5]))