### Problem Statement
'''
Sort the given integers in an array of size "n"

Approach : first loop from 0 to len(arr-1) and
           second loop from i to len(arr) then
           find the smallest number index from second loop and
           swap the numbers in array
'''

### Solution
## Time - O(n^2)
## Space - O(1)
def selectionSort(array):

    for i in range(len(array)-1):
        smallNumIdx = i
        for j in range(i+1,len(array)):
            if array[smallNumIdx] > array[j]:
                smallNumIdx = j
        if smallNumIdx != i:
            array[smallNumIdx],array[i] = array[i], array[smallNumIdx]
    
    print(array)

selectionSort([8, 5, 2, 9, 5, 6, 3])