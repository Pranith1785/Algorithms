### Problem Statement
'''
Function that prints the all the elements in a tree from left to right
i.e., Depth first search

Example: 
Tree =     1
        /     \
       2       3
     /   \    
    4     5     
  

Ans = [1,2,4,5,3]

Depth first search has 

1. In-Order (Left, root,right) - 4,2,5,1,3
2. Pre-Order (root,left,right) - 1,2,4,5,3
3. Post-Order (left,right,root) - 4,5,2,3,1

'''

### Solution -1

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def preOrder(node,array=[]):
    if node is not None:
        array.append(node.value)
        preOrder(node.left)
        preOrder(node.right)

    return array

## Test
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)

print(preOrder(root))

### Acyclic Tree
## Time - O(V+E) | Space - O(V) 
##  V - vertices = node
##  E - edges - b/w two nodes
class Node:
    def __init__(self,name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
    
graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")


print(graph.depthFirstSearch([]))




