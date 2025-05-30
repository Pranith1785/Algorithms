
## Problem statement
'''
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

'''

##Solution 1
## time -  | Space - 

class Node():
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insertNode(self,value):
        curr = self.head
        if curr is None:
            self.head = Node(value)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value)

    def reverseBetween(self,left,right):
        dummy = Node(0,self.head)

        ## reach node at left
        leftprev, curr = dummy, self.head
        for i in range(left-1):
            leftprev = curr
            curr = curr.next

        ## Reverse the node from left to right
        prev = None
        for i in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        ##join the nodes
        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next
    
    def printlist(self,head=None):
        if head is None:
            curr = self.head
        else:
            curr = head
        while curr:
            print(curr.value)
            curr = curr.next
        



ll = LinkedList()
ll.insertNode(3)
ll.insertNode(5)
ll.insertNode(7)
ll.insertNode(9)
ll.insertNode(11)
ll.printlist()
print("==================")
rn = ll.reverseBetween(2,4)
ll.printlist(rn)