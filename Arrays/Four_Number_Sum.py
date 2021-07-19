### Problem Statement
'''
Write a function that takes a non-empty array of distinct integers and target value then
returns all the possible quadruplets in the array that sum up to target value

Example = array = [7, 6, 4, -1, 1, 2]
          Target = 16

        Ans : [[7,6,4,-1],[7,6,1,2]]

'''

### Solution -1
## Time - O(N^4)  | Space - O(N)

def fourNumberSum(array,target):
    quadruplets = []
    for i in range(len(array)-3):
        firstNum = array[i]
        for j in range(i+1,len(array)-2):
            secondNum = array[j]
            for k in range(j+1,len(array)-1):
                thirdNum = array[k]
                for l in range(k+1, len(array)):
                    fourthNum = array[l]
                    if firstNum + secondNum + thirdNum + fourthNum == target:
                        quadruplets.append([firstNum,secondNum,thirdNum,fourthNum])
    
    return quadruplets

### Solution - 2
## Time - O(N^2)  | Space - O(N^2)
###  worst - O(N^3) |       O(N^2)
def fourNumberSum2(array, target):
    
    allPairs = {}
    quadruplets = []

    for i in range(1,len(array)-1):

        for j in range(i+1,len(array)):
            currentSum = array[i] + array[j]
            diffSum = target - currentSum
            if diffSum in allPairs:
                for pair in allPairs[diffSum]:
                    quadruplets.append(pair + [array[i],array[j]])

        for k in range(0,i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairs:
                allPairs[currentSum] = [[array[k],array[i]]]
            else:
                allPairs[currentSum].append([array[k],array[i]])

    return quadruplets


print(fourNumberSum2(array = [7, 6, 4, -1, 1, 2],target = 16))
