### Problem Statement
'''
Write a function which takes an array as input and returns the first duplicate value from the array
if no duplicate record exist return -1

Example: array = [2,1,4,6,2,3,4,8]
         Ans :  2  // 2 and 4 appeared more than once, but 2 appeared first
'''


### Solution - 1
## Time - O(N^2)  | Space - O(1) 

def firstDuplicateValue(array):

    minIndex = len(array)

    for i in range(len(array)):
        value = array[i]
        for j in range(i+1,len(array)):
            valueToCompare = array[j]
            if value == valueToCompare:
                minIndex = min(minIndex, j)

    if minIndex == len(array):
        return -1

    return array[minIndex]    
    

### Solution - 2
## Time - O(N)  |  Space - O(N) 

def firstDuplicateValue2(array):
    dictCount = {}

    for ele in array:
        if ele not in dictCount:
            dictCount[ele] = 0
        dictCount[ele] += 1
        if dictCount[ele] == 2:
            return ele
    return -1

### Solution -3
## Time - O(N) | Space - O(1) 

## Below solution works only if values in array are positive integers
def firstDuplicateValue3(array):

    for value in array:
        absValue = abs(value)

        if array[absValue -1] < 0:
            return absValue
        array[absValue-1] *= -1

    return -1

        
array = [4,8,3,2,1,4,6,2,3,4,8]
print(firstDuplicateValue3(array))
