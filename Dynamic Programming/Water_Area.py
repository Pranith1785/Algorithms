

### Problem Statement
'''
Function that returns the surface area of water trapped b/w pillar(viewed from front end).
Each pillar is of 1unit width and each element in an array represents the height of pillar

Input : height = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
       
Ouptut : 48 units (area)
'''

### Solution - 1
## Time - O(n) | Space - O(n)

def waterArea(arrHeights):

    ## max left pillar height to each index
    leftMaxpillar = [0 for _ in arrHeights]
    rightMaxpillar = [0 for _ in arrHeights]

    leftMax = 0
    for idx in range(len(arrHeights)):
        height = arrHeights[idx]
        leftMaxpillar[idx] = leftMax
        leftMax = max(leftMax,height)

    rightMax = 0
    for idx in reversed(range(len(arrHeights))):
        height = arrHeights[idx]
        rightMaxpillar[idx] = rightMax
        rightMax = max(rightMax,height)

    area = 0
    for idx in range(len(arrHeights)):
        minHeight = min(leftMaxpillar[idx],rightMaxpillar[idx])
        if arrHeights[idx] < minHeight:
            area += minHeight - arrHeights[idx]
    
    return area


### Solution -2 
## Time -  O(n)  | Space - O(1) 

def waterArea2(arrHeights):

    if len(arrHeights) == 0:
        return 0
    
    leftIdx = 0
    rightIdx = len(arrHeights)-1
    leftMax = arrHeights[leftIdx]
    rightMax = arrHeights[rightIdx]
    area = 0

    while(leftIdx < rightIdx):
        if arrHeights[leftIdx] < arrHeights[rightIdx]:
            leftIdx += 1
            leftMax = max(leftMax,arrHeights[leftIdx])
            area += leftMax - arrHeights[leftIdx]
        else:
            rightIdx -= 1
            rightMax = max(rightMax, arrHeights[rightIdx])
            area += rightMax - arrHeights[rightIdx]
        
    return area


print(waterArea2([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))