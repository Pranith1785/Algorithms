### Problem Statement
'''
Function that moves all the instances of an element in array to the end.
Ex : array = [2,3,2,1,5,6,2,2] , element = 2
     output = [3,1,5,6,2,2,2]   
Note : Remaining elements need not be in order
'''

### Solution 1
## Time - O(n^2)
## Space - O(1)

def moveElementToEnd(array,element):

    idx = len(array) -1

    while(idx > 0):
        for i in range(idx-1,-1,-1):
            if array[idx] == element :
                break
            if array[i] == element:
                array[i],array[idx] = array[idx],array[i]
                break
        idx -=1 
    return array

### Solution 2
## Time - O(n)
## Space - O(1)
def moveElementToEnd2(array,element):

    left = 0
    right = len(array)-1

    while(left < right):
        if array[right] == element:
            right -= 1
        if array[left] == element:
            array[left],array[right] = array[right],array[left]
        left += 1
    return array


arr = [2, 1, 2, 2, 2, 3, 4, 2]
toMove =2
print(moveElementToEnd2(arr,toMove))