## Problem Statement
'''
Function that returns the array of length two representing the largest range in the given array.
Array records need not to be in sorted order

Ex : Array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
     Ans = [0,7]
'''

## Solution 1
## Time - O(nlogn)
## Space - O(1)
def largestRange(array):

    array.sort()

    longestRange, currentRange = 0, 1
    first_num, last_num = array[0], array[0] 
    bestRange = []

    if len(array) ==1:
        return [array[0],array[0]]

    for idx in range(0,len(array)-1):
        if array[idx] == array[idx+1] or array[idx+1] - array[idx] == 1:
            last_num = array[idx+1]
            currentRange += 1
        else:
            if currentRange > longestRange:
                longestRange = currentRange
                bestRange = [first_num,last_num]
            first_num = array[idx]
            last_num = array[idx]
            currentRange = 1

    return bestRange

## Solution 2
## Time - O(n)
## Space - O(n)
def largestRange2(array):

    num_dict = {}
    bestRange = []
    for val in array:
        num_dict[val] = False

    longestRange = 0
    for num in array:
        if num_dict[num] :
            continue
        num_dict[num] = True
        currentRange = 1
        left_num = num - 1
        right_num = num + 1

        while left_num in num_dict:
            num_dict[left_num] = True
            left_num -= 1
            currentRange += 1
        
        while right_num in num_dict:
            num_dict[right_num] = True
            right_num += 1
            currentRange += 1
        if currentRange > longestRange:
            longestRange = currentRange
            bestRange = [left_num+1, right_num-1]
    return bestRange



num_array = [1, 2]
print(largestRange(num_array))
print(largestRange2(num_array))
