### Problem Statement
'''
Function that validates the Binary Search Tree

'''

### Solution -1
## Time - O(N) | Space - O(d) - depth of the tree

class BST:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None


def validateBst(root):
    return validateBstHelper(root,float("-inf"), float("inf"))

def validateBstHelper(node,minValue,maxValue):
    if node is None:
        return True
    
    if node.value < minValue or node.value > maxValue:
        return False
    
    leftValidate = validateBstHelper(node.left,minValue,node.value)
    rightValidate = validateBstHelper(node.right, node.value, maxValue)

    return leftValidate and rightValidate
