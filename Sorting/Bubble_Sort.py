### Problem Statement
'''
Sort the array of given integers

Approach : Traverse thr the array(outer loop) and again loop thru length of array minus outer loop element,
        then swap the elements if number is bigger than next number
'''

### Problem 1
# Time - O(n^2) | Best time - O(n)
# Space - O(1)
def bubbleSort(array):

    for i in range(len(array)):
        swapCheck = False
        for j in range(0,len(array)-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapCheck = True
        if not swapCheck :
            return array


### Solution 2
## Time - O(n^2)
## Space - O(1)
def bubbleSort2(array):
    swapCheck = False
    counter = 0
    while(not swapCheck):
        swapCheck = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                swapCheck = False
        counter += 1
    return array

arr =  [427,-153, 240,-160,-610, -583,-27, 131]
print(bubbleSort2(arr)) 