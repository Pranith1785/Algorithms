
### Problem Statement
'''
Function that returns the number of ways to traverse the graph from top left corner to bottom right corner
Only right and down are allowed 

Input : height = 3
        width = 4
        
       
Ouptut : 10 ways
'''

### Solution 1
## Time - O(n*m) | Space -O(n*m) 

def numberOfWaysToTraverseGraph(width,height):

    ways = [[0 for _ in range(width+1)] for _ in range(height+1)]  ##creating an extra height and width
    print(ways)
    for widthIdx in range(1,width+1):
        for heightIdx in range(1,height+1):
            if widthIdx == 1 or heightIdx == 1:
                ways[heightIdx][widthIdx] = 1
            else:
                waysleft = ways[heightIdx][widthIdx-1]
                waysUp = ways[heightIdx-1][widthIdx]
                ways[heightIdx][widthIdx] = waysleft + waysUp

    return ways[height][width]


height = 3
width = 4
print(numberOfWaysToTraverseGraph(width,height))