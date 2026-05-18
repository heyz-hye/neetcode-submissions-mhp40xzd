
class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.table={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self, node):
        pre=node.prev
        nxt=node.next
        pre.next=nxt
        nxt.prev=pre


    def insert(self, node):
        pre=self.right.prev
        pre.next=node
        node.prev=pre
        node.next=self.right
        self.right.prev=node

    def get(self, key: int) -> int:
        if key in self.table:
            self.remove(self.table[key])
            self.insert(self.table[key])
            return self.table[key].value

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.remove(self.table[key])
        self.table[key]=Node(key,value)
        self.insert(self.table[key])

        if self.capacity<len(self.table):
            lru=self.left.next
            self.remove(lru)
            del self.table[lru.key]




        
