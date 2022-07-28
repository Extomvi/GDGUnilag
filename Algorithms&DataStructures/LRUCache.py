"""
LRU Cache design problem
"""

class Node:

    def __init__(self, key, val):
        self.val = key
        self.val = val
        self.prev = None
        self.next = None

class LRU:

    def __init__(self, capacity):
        self.capacity = capacity

        #using a hashmap to map of the key and values
        self.cache = {}

        #least recently used, left pointer
        self.left = Node(0,0)

        #most recently used, right pointer
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    #helper function to remove node from list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    #helper function to insert node at right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev


    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            #removing from the list and delete the LRu from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
