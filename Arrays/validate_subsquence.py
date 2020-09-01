### Problem Statement
'''
Given two non empty arrays, Function that determines whether second array is subsequence of first array 
'''

### Solution 1
# Time Complexity - O(n^2)
# Space Complexity - O(1) 
def isValidSubsequence1(firstArray, sequenceArray):

    i = 0 
    for ele in sequenceArray:
        eleFlag = False
        if i <= len(firstArray)-1:
            for j in range(i,len(firstArray)):
                if firstArray[j] == ele:
                    i = j+1
                    eleFlag = True
                    break
                if j == len(firstArray)-1 and not eleFlag:
                    return False
        else:
            return False

    return True

### Solution 1
# Time Complexity - O(n)
# Space Complexity -  O(1)
def isValidSubsequence2(firstArray,sequenceArray):

    arrInc = 0
    seqArrInc = 0

    while arrInc < len(firstArray) and seqArrInc < len(sequenceArray) :
        if firstArray[arrInc] == sequenceArray[seqArrInc]:
            seqArrInc += 1
        arrInc += 1
    
    return seqArrInc == len(sequenceArray)

### Solution 1
# Time Complexity - O(n)
# Space Complexity -  O(1)
def isValidSubsequence3(firstArray,sequenceArray):
    seqArrInc = 0
    for value in firstArray :
        if seqArrInc == len(sequenceArray):
            break
        if value == sequenceArray[seqArrInc] :
            seqArrInc += 1
    
    return seqArrInc == len(sequenceArray)



firstArray = [5, 1, 10]
sequenceArray = [5, 1,9]

print(isValidSubsequence2(firstArray,sequenceArray))
        
