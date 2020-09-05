### Problem Statement
'''
Find all the possible triplets from an array of length "n", whose sum is equal to "k"
'''


### Solution 1
# Time - O(n^2 + log(n)) -> O(n^2)
# Space - O(n)
def threeNumberSum(array,target):

    array.sort()      ## O(log(n))
    arrSize = len(array) 
    arrTriplets = []
    for i in range(arrSize-2):   ## O(n)
        num1 = array[i]
        leftIdx = i+1
        rightIdx = arrSize-1
        while(leftIdx < rightIdx):        ## O(n)
            num2 = array[leftIdx]
            num3 = array[rightIdx]
            if target > num1 + num2 + num3 :
                leftIdx += 1
            elif target < num1 + num2 + num3:
                rightIdx -= 1
            else:
                arrTriplets.append([num1,num2,num3])
                leftIdx += 1
                rightIdx -= 1
    return arrTriplets

array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(threeNumberSum(array,target))



