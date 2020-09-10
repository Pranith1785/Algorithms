### Problem Statemen
'''
Construct a doubly Linked list 
'''

### Solution
class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        
    ## Time - O(1) | Space - O(1)
    def setHead(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head,node)

    ## Time - O(1) | Space - O(1)   
    def setTail(self,node):
        if self.tail is None:
             ## self.setHead(node) # we can use sethead function or below code
            self.tail = node 
            self.head = node
            return
        self.insertAfter(self.tail,node)

    ## Time - O(1) | Space - O(1)
    def insertBefore(self,node,nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    ## Time - O(1) | Space - O(1)
    def insertAfter(self,node,nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    ## Time - O(n) | Space - O(1)
    def insertAtPosition(self,position,nodeToInsert):

        if position == 1:
            self.setHead(nodeToInsert)
            return
        
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node,nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    ## Time - O(n) | Space - O(1)
    def removeNodesWithValue(self,value):
        node = self.head
        while node is not None:
            nodeToRemove = node  
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
            
    ## Time - O(1) | Space - O(1)
    def remove(self,node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        
        if node.prev is not None:
            node.prev.next = node.next
        
        if node.next is not None:
            node.next.prev = node.prev

        node.next = None
        node.prev = None
        
    ## Time - O(n) | Space - O(1)
    def containsNodeWithValue(self,value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None
