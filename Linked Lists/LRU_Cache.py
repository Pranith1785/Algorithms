### Problem Statement
'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
evict the least recently used key.

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

'''

## Solution 1
## Time - O(1)   | Space - O(n)

class Node():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev, self.next = None, None

class LRUCache():
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.cache = {}
        ## Left - least recently used, right - most recently used
        self.left, self.right = Node(0,0), Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left


    ##Remove the Node from list
    def removeNode(self,node):
        prv, nxt = node.prev , node.next
        prv.next, nxt.prev = nxt, prv
    
    ## Insert the node at right
    def insertNode(self,node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt

    ## Get the value from key and also make the key as most recent
    def get(self,key):

        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
            return self.cache[key].value
       
        return -1
        
    ## if key doesnt exist add to list, if capacity exceeds remove LRU and add node to last
    ## if key already exists, move the node to last and update the value 
    def put(self,key, value) :

        if key in self.cache:
            self.removeNode(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insertNode(self.cache[key]) 

        if len(self.cache)  > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.removeNode(lru)
            



lrc = LRUCache(2)
lrc.put(1,1)
lrc.put(2,5)
print(lrc.get(2))
lrc.put(1,3)
print(lrc.get(1))
lrc.put(5,8)
print(lrc.get(2))

