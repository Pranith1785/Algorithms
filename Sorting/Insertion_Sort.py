### Problem Statement
'''
Sort the given integers in an array of size "n"

Approach : First loop(i) starts from 1 to length of array and second loop from i to 0,
        then swap the element if are in not in sorted order
'''

### Solution 
# Time - worst case O(n^2) | average O(n)
# Space - O(1)
def insertionSort(array):

    for i in range(1,len(array)):
        j = i 
        while(j>0 and array[j-1] > array[j]):
            array[j-1],array[j] = array[j],array[j-1]
            j -= 1
    return array


arr = [427,-153, 240,-160,-610, -583,-27, 131]
print(insertionSort(arr))
