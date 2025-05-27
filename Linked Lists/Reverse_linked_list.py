
### Problem statement
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

'''

class Node():
    def __init__(self,value=0,next=None) -> None:
        self.value = value
        self.next = next


class SingleLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.rev = None

    ## add new data at the end
    def insertNodeAtEnd(self,new_data):
        new_node = Node(new_data)
        curr = self.head
        if curr is None:
            self.head = new_node
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    ## reverse linked list
    ## time - O(N) | space - O(1)
    def reverseList(self):
        prev, curr = None, self.head

        while curr :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        self.rev = prev


    def printList(self,rev=False):
        if not rev:
            curr = self.head
        else:
            curr = self.rev

        while curr is not None:
            print(curr.value)
            curr = curr.next


sl = SingleLinkedList()
sl.insertNodeAtEnd(1)
sl.insertNodeAtEnd(3)
sl.insertNodeAtEnd(5)

sl.printList()

sl.reverseList()

sl.printList(rev=True)
