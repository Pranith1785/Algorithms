### Problem
'''
Distance b/w a node in a binary tree and the tree's root is called Node distance.
Function takes binary tree and returns the sum of its nodes depth.  
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

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


## Solution -1 
## Time - O(N) | Space - O(h) - height of tree

def nodeDepth(node,sumDepths=0):
    
    if node is None:
        return 0

    return sumDepths + nodeDepth(node.left, sumDepths+1) + nodeDepth(node.right, sumDepths+1)

## Solution - 2
## Time - O(N) | Space - O(h)

def nodeDepth1(node):
    sumDepths = 0
    stack = [{"node":node,"depth":0}]

    while len(stack) > 0 :
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"] , nodeInfo["depth"]

        if node is None:
            continue

        sumDepths += depth
        stack.append({"node":node.left, "depth": depth+1})
        stack.append({"node":node.right, "depth": depth+1})

    return sumDepths


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)

print(nodeDepth(root))
print(nodeDepth1(root))