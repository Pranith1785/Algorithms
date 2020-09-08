### Problem Statement
'''
In a given two-dimensional array/matrix, each row and column is sorted and whose width and height ar not same,
Find the target element position in array/martix if exists else [-1,-1]
'''

### Solution 1
## Time - O(n*m) - n-rows,m-columns
## Space - O(1)
def searchInSortedMatrix(array,target):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == target:
                return [i,j]
    return [-1,-1]

### Solution 2
## Time - O(n+m)
## Space - O(1)

def searchInSortedMatrix2(array,target):
    row = 0
    col = len(array[0])-1

    while(row < len(array) and col >= 0):
        value = array[row][col]
        if value < target:
            row += 1
        elif value > target :
            col -= 1
        else:
            return [row,col]
    return [-1,-1]
    

matrix = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004]
]

print(searchInSortedMatrix2(matrix,1035))