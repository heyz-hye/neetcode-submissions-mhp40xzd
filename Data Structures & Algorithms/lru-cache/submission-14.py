class Node:
    def __init__(self,key,value,next,prev):
        self.value=value
        self.key=key
        self.next=None
        self.prev=None


class LRUCache:

    def __init__(self, capacity: int):
        self.left=Node(0,0,None,None)
        self.right=Node(0,0,None,None)
        self.left.next=self.right
        self.right.prev=self.left
        self.table={}
        self.capacity=capacity
    
    def remove(self,node):
        pre=node.prev
        nxt=node.next
        pre.next=nxt
        nxt.prev=pre
    
    def insert(self,node):
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
            self.table[key].value=value
            self.remove(self.table[key])
        else:
            self.table[key]=Node(key,value,None,None)
        self.insert(self.table[key])

        if len(self.table)>self.capacity:
            node=self.left.next
            self.remove(node)
            del self.table[node.key]
        
