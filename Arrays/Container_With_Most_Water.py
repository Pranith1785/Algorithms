### Problem Statement
'''
Write a function that takes an interger array of heights  of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]) 

Return the maximum amount of water a container can store.

Example :  height = [1,8,6,2,5,4,8,3,7]
           Ans = 49 
           distance b/w indexes (8-1) and min of vertical lines (8,7) 

'''

## Solution - 1
## Time -  O(n) , Space - O(1)
def maxArea(height: list[int]) -> int:
    maxArea = 0
    leftIdx = 0
    rightIdx = len(height)-1

    while(leftIdx < rightIdx):
        maxArea = max(maxArea, min(height[leftIdx],height[rightIdx])* (rightIdx-leftIdx))

        if height[leftIdx] < height[rightIdx]:
            leftIdx += 1
        elif height[leftIdx] >= height[rightIdx]:
            rightIdx -= 1
            
    return maxArea


height = [1,8,6,2,5,4,8,3,7]
print("Area is -", str(maxArea(height)))