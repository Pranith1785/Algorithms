### Problem Statement

'''
Write a function that takes n*m two dimensional array and 
returns a one-dimensional array of all elements in zigzag order.

zigzag order starts at top left corner of 2dimensional array and goes down by one element and
proceeds in zigzag pattern all the way to bottom right corner.

Ex : array = [
                [1, 3, 4, 10],
                [2, 5, 9, 11],
                [6, 8, 12, 15],
                [7, 13, 14, 16]
            ]

    Ans = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

'''

### Solution -1
## Time - O(n+m)  | Space - O(n+m)
    
def isOutOfBounds(row,col,height,width):
    return row < 0  or row > height or col < 0 or col > width

def zigzagTraverse(array):

    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    nrow, ncol = 0, 0
    downSide = True

    while not isOutOfBounds(nrow,ncol,height,width):
        result.append(array[nrow][ncol])
        if downSide:
            if ncol == 0 or nrow == height:
                downSide = False
                if nrow == height:
                    ncol += 1
                else:
                    nrow += 1
            else:
                ncol -= 1
                nrow += 1
        else:
            if nrow == 0 or ncol == width:
                downSide = True
                if ncol == width:
                    nrow += 1
                else:
                    ncol += 1
            else:
                nrow -= 1
                ncol += 1

    return result
                

    
array = [
            [1, 3, 4, 10],
            [2, 5, 9, 11],
            [6, 8, 12, 15],
            [7, 13, 14, 16]
        ]

print(zigzagTraverse(array))