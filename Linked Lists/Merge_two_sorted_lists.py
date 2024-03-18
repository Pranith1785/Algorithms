
### Problem Statement
'''
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

'''

### Solution -1
## Time -      | Space - 


class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        
class LinkedList():

    def mergeList(self,l1 : [Node], l2 : [Node]) -> [Node] :

        finalNode = Node(0)
        curr = finalNode

        while l1 or l2:
            
            val1 = l1.value if l1 else float("infinity")
            val2 = l2.value if l2 else float("infinity")

            if val1 <= val2:
                curr.next = Node(value=val1)
                l1 = l1.next if l1 else None
            else:
                curr.next = Node(value=val2)
                l2 = l2.next if l2 else None
            
            curr = curr.next

        return finalNode.next
    
N1 = Node(2)
#N1.next = Node(3)

N2 = Node(1)
N2.next = Node(4)

res = LinkedList()
resNode = res.mergeList(N1,N2)

while resNode:
    print(resNode.value)
    resNode = resNode.next


