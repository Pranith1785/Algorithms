### Problem Statement
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water

Example :
Input : grid = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
               ]
Output: 3

'''

## Solution - 1
## Time -    | Space - 
import collections
def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islandsCount = 0
    visited = set()

    def bfs(r,c):
        q = collections.deque()
        visited.add((r,c))
        q.append((r,c)) 

        while q:
            row, col = q.popleft()
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if (r in range(rows) and c in range(cols) and 
                    (r,c) not in visited and
                    grid[r][c] == "1"):

                    visited.add((r,c))
                    q.append((r,c))


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c)
                islandsCount += 1
        
    return islandsCount
        

grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
       ]

print(numIslands(grid))