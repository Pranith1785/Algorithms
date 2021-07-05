## Problem Statement :
'''
Function takes the Binary tree and target value and returns the closet value to target value.
Example :
tree =     1
        /     \
       12       23
     /   \    /  \
    4     16  8    26  
   / \   / 
  1   9 13
Target Value = 14
Answer = 13
'''
class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.rigt = None


### Solution -1
## Avg Time - O(log(N)) |  Avg Space - O(log(N)) 
## Worst Time - O(N) | Worst Space - O(N)  

def closestValueInBST(tree,target):
    return closestValueInBSTHelper(tree,target,tree.value)    

def closestValueInBSTHelper(tree,target,closestValue):

    if tree is None:
        return closestValue
    
    if abs(target - closestValue) > abs(target-tree.value):
        closestValue = tree.value
    
    if target < tree.value:
        return closestValueInBSTHelper(tree.left,target,closestValue)
    elif target > tree.value:
        return closestValueInBSTHelper(tree.right, target, closestValue)
    else:
        return closestValue


### Solution -2
## Time - O(log(N))    | Space - O(1)

def closestValueInBST1(tree,target):
    return closestValueInBSTHelper1(tree,target,tree.value)

def closestValueInBSTHelper1(tree,target,closestValue):
    currentNode = tree
    while currentNode is not None:
        
        if abs(target - closestValue) > abs(target - currentNode.value):
            closestValue = currentNode.value
        
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    
    return closestValue    


## Test
root = BinaryTree(10)
root.left = BinaryTree(5)
root.left.left = BinaryTree(2)
root.left.left.left = BinaryTree(1)
root.left.right = BinaryTree(5)
root.right = BinaryTree(15)
root.right.left = BinaryTree(13)
root.right.left.right = BinaryTree(14)
root.right.right = BinaryTree(22)

target = 12
print(closestValueInBST1(root,target))