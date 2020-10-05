### Problem Statement
'''
Find the length of strictly increasing or decreasing elements 
        followed by one decreasing or increasing element in an array
constraints - atleast 3 integers required to form peak 

example : Array - [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
          ans - 6 //[4, 0, 10, 6, 5, -1, -3] 
'''

## Approach :
'''
1. First find the peak node in the array
2. traverse back to left side from peak and to right side from peak until the peak condition satisfy
'''

## Solution 1
# Time - O(n) | Space - O(1)
def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array)-1:
        isPeak = array[i] > array[i-1] and array[i] > array[i+1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i-2
        while(leftIdx >=0 and array[leftIdx] < array[leftIdx+1]):
            leftIdx -= 1
        
        rightIdx = i+2
        while(rightIdx < len(array) and array[rightIdx-1]>array[rightIdx]):
            rightIdx += 1
        
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength,currentPeakLength)
        i = rightIdx
    
    return longestPeakLength


arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(arr))


