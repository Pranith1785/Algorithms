### Problem Statement
'''
56. Merge Intervals

Function that takes non-empty array of arbitrary intervals then merges the overlapping intervals and
returns the new intervals

Example : array = [[1,2],[3,5],[4,7],[6,8],[9,10]]
          ans = [[1,2],[3,8],[9,10]]

'''

### Solution -1
## Time - O(NlogN) | Space - O(N) 

def mergeOverlappingIntervals(array):

    sortedArray = sorted(array,key=lambda x:x[0])

    mergedIntervals = []
    currentIntervals = sortedArray[0]
    mergedIntervals.append(currentIntervals)

    for nextInterval in sortedArray:
        currentIntervalStart , currentIntervalEnd = currentIntervals
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentIntervals[1] = max(currentIntervalEnd,nextIntervalEnd)
        else:
            currentIntervals = nextInterval
            mergedIntervals.append(nextInterval)
    
    return mergedIntervals


arrayIntervals = [[1, 2],[3, 5],[4, 7],[6, 8],[9, 10]]
print(mergeOverlappingIntervals(arrayIntervals))

