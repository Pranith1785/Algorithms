### Problem Statement
'''
Find the three largest numbers from a given array
'''

### Solution 1
## Time - O(nlog(n))
## Space - O(1)

def findThreeLargestNumbers(array):
    array.sort()
    return array[-3:]


### Solution 2
## Time - O(3n) -> O(n)
## Space - O(1)

def findThreeLargestNumbers2(array):
    arrLargestNum = [None,None,None]

    for num in array:
        if arrLargestNum[2] is None or num > arrLargestNum[2]:
            updateArray(arrLargestNum,num,2)
        elif arrLargestNum[1] is None or num > arrLargestNum[1]:
            updateArray(arrLargestNum,num,1)
        elif arrLargestNum[0] is None or num > arrLargestNum[0]:
            updateArray(arrLargestNum, num , 0)
    
    return arrLargestNum

def updateArray(arrNums, num, idx):

    for i in range(idx+1):
        if i == idx:
            arrNums[i] = num
        else:
            arrNums[i] = arrNums[i+1]



array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

print(findThreeLargestNumbers2(array))