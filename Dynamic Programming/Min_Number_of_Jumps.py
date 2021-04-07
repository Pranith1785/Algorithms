## Problem Statement
'''
Find Minimum number of jumps required to reach the final index of an array.
Given a non-empty array of positive integers 
where each integer represents the maximum no of steps you can take forward in array

Jumping from idx to idx + x is considered as 1 jump.

Example : In an array element at Index 1 is 3, so you can go from index 1 to 2, 3 or 4.

    Array  = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
    Ans = 4 (3 -> (4 or 2) -> (2 or 3) -> 7 -> 3)

'''

## Solution -1
## Time - O(n^2)
## Space - O(n)
def minNumberOfJumps(array):

    jumps = [float('inf') for x in array]
    jumps[0] = 0

    for i in range(1,len(array)):        
        for j in range(0,i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[j]+1,jumps[i])
    
    return jumps[-1]


## Solution - 2
## Time - O(n)
## Space - O(1)

def minNumberOfJumps2(array):

    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1,len(array)-1):
        maxReach = max(maxReach, array[i] + i )
        steps -= 1

        if steps == 0:
            jumps += 1
            steps = maxReach - i

    return jumps+1


array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
#array = [1,1]
print(minNumberOfJumps(array))
print(minNumberOfJumps2(array))