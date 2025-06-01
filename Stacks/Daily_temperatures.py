## Problem statement
'''
739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

'''

## Solution 1
## Time - O(n)  | Space - O(n)

def dailyTemp(tempList):

    result = [0] * len(tempList)
    stack = [] ## pair temp and index

    for i, tempVal in enumerate(tempList):

        while stack and tempVal > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            result[stackIndex] = i-stackIndex
        
        stack.append([tempVal,i])

    return result

## Solution - 2
## Time - O(n)   | Space - O(n)

def dailyTemp2(temperatures):

    n = len(temperatures)
    res = [0]*n

    maxTemp = temperatures[-1]

    for i in range(n-1-1,-1,-1):
        if temperatures[i] > maxTemp:
            maxTemp = temperatures[i]
        else:
            interval = 1
            while temperatures[i] > temperatures[i+interval]:
                interval += res[i+interval]
            res[i] = interval
    
    return res


temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemp2(temperatures))
