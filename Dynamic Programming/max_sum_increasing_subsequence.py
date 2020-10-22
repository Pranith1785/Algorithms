### Problem Statement
'''
Function which gives the max sum increasing subsequence in an non-empty array

Example : array = [10,70,20,50,30,45]
          ans = 105 ([10,20,30,45] subsequence array which has maximum sum)

'''

## Solution - 1
## Time - O(n*n)
## Space - O(n)
def maxSumIncreasingSubsequence(array):
    sumArr = [num for num in array]
    sequences = [None]*len(array)
    maxSumIdx = 0
    for idx in range(len(array)):
        currNum = array[idx]
        for i in range(0,idx):
            num = array[i]
            if currNum > num and currNum + sumArr[i] >= sumArr[idx]:
                sumArr[idx] = currNum + sumArr[i]
                sequences[idx] = i
        if sumArr[idx] >= sumArr[maxSumIdx]:
            maxSumIdx = idx
    
    return [sumArr[maxSumIdx],buildSequence(array,sequences,maxSumIdx)]

def buildSequence(array,sequences,currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))

arr = [-1, 1]
print(maxSumIncreasingSubsequence(arr))




