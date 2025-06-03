## Problem statement
'''
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

'''

## Solution - 1
## Time - O(n)    | Space - O(n)
def insertIntervals(intervals, newInterval):

    finalInterval = []
   
    for i in range(0, len(intervals)):
        
        currArray = intervals[i]
        currStart, currEnd = currArray[0], currArray[1]
        newIntStart, newIntEnd = newInterval[0], newInterval[1]

        if newIntEnd < currArray[0]:
            finalInterval.append(newInterval)
            return finalInterval + intervals[i:]
        elif newIntStart > currEnd :
            finalInterval.append(currArray)
        else:
            newInterval = [min(newIntStart, currStart), max(newIntEnd,currEnd)]
    
    finalInterval.append(newInterval)

    return finalInterval


intervals = [[1,3],[6,9]]
newInterval =[-1,0]

print(insertIntervals(intervals, newInterval))
