### Problem Statement
'''
Function that takes array of atleast two integers and returns an array of starting and
ending indices of the smallest subarray in an input that needs to be sorted(ascending)

if the array is already sorted then return [-1,1]

Example : Array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
          Ans   = [3,9] // from index 3 and 9 the array need to be sorted

'''

### Solution -1
## Time - O(N^2) | Space - O(1) 

import math

def subarraySort(array):

    minIdx, maxIdx = float('inf') , float('-inf')

    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                minIdx = min(i, minIdx)
                maxIdx = max(j, maxIdx)
    if math.isinf(minIdx) :
        return [-1,-1]
    else:
        return [minIdx,maxIdx] 


### Solution - 2
## Time -  | Space - 

def subarraySort2(array):
    minNum , maxNum = float('inf') , float('-inf')

    for i in range(len(array)):
        num = array[i]
        if checkNumberOrder(i,num,array):
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)

    if minNum == float('inf') :
        return [-1,-1]
    
    subarrayLeftIdx = 0
    while minNum >= array[subarrayLeftIdx]:
        subarrayLeftIdx += 1
    
    subarrayRightIdx = len(array)-1
    while maxNum <= array[subarrayRightIdx]:
        subarrayRightIdx -= 1

    return [subarrayLeftIdx,subarrayRightIdx]
     

def checkNumberOrder(i,num,array):
    if i == 0:
        return num > array[i+1]
    elif i == len(array) -1:
        return num < array[i-1]
    return num > array[i+1] or num < array[i-1]



arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

print(subarraySort2(arr))


