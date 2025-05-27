
## Problem statement
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
list1 = [2,4,3], list2 = [5,6,4]

Ans = [7,0,8]

Explaination :  l1 + l2 = 342 + 465 = 807
    linked list will be = [7,0,8]

'''

class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


## Add two linked list
def add_two_numbers(l1 : [ListNode], l2 : [ListNode]) -> [ListNode] :

    finalNode = ListNode()
    curr = finalNode

    carryVal = 0
    while l1 or l2 or carryVal > 0 :

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        val3 = val1 + val2 + carryVal
        ## updating
        carryVal = val3 // 10
        val3 = val3 % 10

        ## updating linked list nodes
        curr.next = ListNode(val3)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        curr = curr.next

    return finalNode.next




















