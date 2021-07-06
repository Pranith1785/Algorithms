'''
BST class that supports inserting, removing or searching a value

Note : left node values are strictly less than the root node value
       right node values are strictly greater than or equal to the root node value.

      Can't remove the value when there is single node

Example :
tree =     10
        /     \
       5       23
     /   \    /  \
    3     8  13    26  
   / \   / 
  1   4 6

'''

### Solution -1

class BST:
    def __init__(self,value) :
        self.value = value
        self.left = None
        self.right = None
    
    ## Time - O(log(N)) avg  | space - O(1)
    ## Time - O(N) worst     | Space - O(1)
    def insert(self,value):
        newNode = self
        while True:
            if newNode.value <= value:
                if newNode.right is None:
                    newNode.right = BST(value)
                    break
                else:
                    newNode = newNode.right
            else:
                if newNode.left is None:
                    newNode.left = BST(value)
                    break
                else:
                    newNode = newNode.left
        return self

    ## Time - O(log(N)) avg  | space - O(1)
    ## Time - O(N) worst     | Space - O(1)
    def contains(self,value):    
        newNode = self
        while newNode is not None:
            if newNode.value > value:
                newNode = newNode.left
            elif newNode.value < value:
                newNode = newNode.right
            else:
                return True
        return False

    ## Time - O(log(N)) avg  | space - O(1)
    ## Time - O(N) worst     | Space - O(1)
    def remove(self,value,parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left  
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
                
            else:
                ## value has two node values
                if currentNode.left is not None and currentNode.right is not None:
                    ## assign the node value with the smallest value in the right of the tree (leftmost value of right tree)
                    currentNode.value = currentNode.right.getMinValue()
                    ## now remove the min value of the right of tree
                    currentNode.right.remove(currentNode.value,currentNode)

                ## if value has not parentNode
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        ## remove the single root node
                        ## currentNode.value = None
                        pass

                ## value has only one node value 
                elif parentNode.left == currentNode:
                    if currentNode.left is not None:
                        parentNode.left = currentNode.left
                    else:
                        parentNode.left = currentNode.right
                ## value has only one node value 
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
                break

        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

                
                







    

root = BST(10)
root.insert(15)
root.insert(12)
root.insert(18)
root.insert(5)
root.insert(2)

print(root.value)
print(root.contains(4))



