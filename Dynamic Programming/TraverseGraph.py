
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


### Solution 2
## Time - O(2^(n+m)) | Space - O(n+m)

def numberOfWaysToTraverseGraph2(width,height):
    if width == 1 or height ==1:
        return 1
    
    return numberOfWaysToTraverseGraph2(width-1,height) + numberOfWaysToTraverseGraph2(width,height-1)


### Solution 3
## Time - O(n+m) | Space - O(1)

def factorial(num):
    if num == 1:
        return 1
    result = 1
    for n in range(2,num+1):
        result *= n
    
    return result

def numberOfWaysToTraverseGraph3(width,height):
    xDistanceToCorner = width-1
    yDistanceToCorner = height -1

    numerator = factorial(xDistanceToCorner + yDistanceToCorner)
    denominator = factorial(xDistanceToCorner) * factorial(yDistanceToCorner)

    return(numerator//denominator)




height = 3
width = 4
print(numberOfWaysToTraverseGraph3(width,height))