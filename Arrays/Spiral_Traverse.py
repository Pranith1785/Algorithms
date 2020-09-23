### Problem Statement
'''
Function thats take two dimensional array (n*m) and returns the one dimensional array 
of all array elements in a spiral order
'''
### Solution - 1
#Time - O(n) 
# Space - O(n)
def spiralTraverse(array):
    startRow, endRow = 0, len(array)-1
    startCol , endCol = 0, len(array[0])-1
    result = []
    while(startRow <= endRow and startCol <= endCol):
        for col in range(startCol,endCol+1):
            result.append(array[startRow][col])

        for row in range(startRow+1,endRow+1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol,endCol)):
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        for row in reversed(range(startRow,endRow)):
            if startCol == endCol:
                break
            result.append(array[row][startCol])
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return result        


print(spiralTraverse([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))