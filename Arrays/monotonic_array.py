## Problem Statement
'''
Find whether a given array is monotonic or not
monotonic : either non-increasing or non-decreasing
'''

### Solution - 1
## Time - O(n)
## Space - O(1)
def isMonotonic(array):

    count = len(array)
    if count < 2:
        return True 
    actualTrend = getTrend(array[0],array[1])
    for i in range(2,len(array)):
        newTrend = getTrend(array[i-1],array[i])
        if newTrend != "equal":
            if actualTrend == "equal":
                actualTrend = newTrend
            elif newTrend != actualTrend :
                return False
    return True
        
            
def getTrend(eleFirst,eleSecond):
    if eleFirst > eleSecond:
        return "negative"
    elif eleFirst < eleSecond:
        return "positive"
    else:
        return "equal"


### Solution - 2
# Time - O(n)
# Space - O(1)
def isMonotonic1(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            isNonDecreasing = False
        elif array[i] > array[i-1]:
            isNonIncreasing = False
    return isNonDecreasing or isNonIncreasing


### Solution - 3
## Time - O(n)
## Space - O(1)
def isMonotonic2(array):
    if len(array) < 2:
        return True
    trend = array[1] - array[0]
    for i in range(2,len(array)):
        if trend == 0:
            trend = array[i] - array[i-1]
            continue
        if checkTrend(trend,array[i-1],array[i]):
            return False
    return True

def checkTrend(oldTrend,prev_Value,curr_Value):
    diff = curr_Value - prev_Value
    if oldTrend > 0 :
        return diff < 0 
    return diff > 0



arr = [-1, -1, -2, -3, -4, -5, 5, -5, -6, -7, -8, -8, -9, -10, -11]
print(isMonotonic2(arr))