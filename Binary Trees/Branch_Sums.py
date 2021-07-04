### Problem
'''
Function that takes binary tree as input and returns the list of branch sums ordered form leftmost to rightmost.
Example :
tree =     1
        /     \
       2       3
     /   \    /  \
    4     5  6    7   
   / \   / 
  8  9  10

Answer = [15,16,18,10,11] 
'''

### Solution - 1
## Time - O(N)  |  Space - O(N) N- number of nodes  

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calculatedBranchSums(root,0,sums)
    return sums


def calculatedBranchSums(node,runningSum, sums):
    if node is None:
        return
    runningSum += node.value
    if node.left is None and node.right is None:
        sums.append(runningSum)
        return

    calculatedBranchSums(node.left,runningSum,sums)
    calculatedBranchSums(node.right, runningSum, sums)


## Test
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)


print(branchSums(root))


