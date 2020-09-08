### Problem Statement
'''
Find the pair of numbers(from each array) whose absolute difference is closest to Zero,
and returns array of two numbers
'''

### Solution 1
## Time - O(nlog(n) + mlog(m) + n) -> O(nlog(n) + mlog(m))
## Space - O(1)
def smallestDifference(array1, array2):

    array1.sort()   ##TIme - O(nlog(n))
    array2.sort()   ##Time - O(mlog(m))

    idx1, idx2 = 0, 0
    smallDiff , currentDiff = float("inf") , float("inf")

    smallestPair = []

    while( idx1 < len(array1) and idx2 < len(array2)):   ##can be O(n) or O(m)
        firstNum = array1[idx1]
        secondNum = array2[idx2]
        if firstNum > secondNum :
            idx2 += 1
            currentDiff = firstNum - secondNum
        elif firstNum < secondNum :
            currentDiff = secondNum - firstNum
            idx1 += 1
        else:
            return [firstNum,secondNum]
        if smallDiff > currentDiff:
            smallDiff = currentDiff
            smallestPair = [firstNum,secondNum]
    
    return smallestPair


array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]

print(smallestDifference(array1,array2))