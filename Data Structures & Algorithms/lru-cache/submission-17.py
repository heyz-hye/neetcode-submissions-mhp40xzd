class Node:
    def __init__(self,key,val,pre,next):
        self.key=key
        self.val=val
        self.pre=pre
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.left=Node(0,0,None,None) #right didnt exist yet so you need to assign pointer after
        self.right=Node(0,0,None,None)
        self.left.next=self.right
        self.right.pre=self.left
        self.table={}
        

    def remove(self,node):
        nxt=node.next
        prev=node.pre
        prev.next=nxt
        nxt.pre=prev

    def insert(self,node):
        temp=self.right.pre
        temp.next=node
        node.pre=temp
        node.next=self.right
        self.right.pre=node

    def get(self, key: int) -> int:
        if key in self.table:
            self.remove(self.table[key])
            self.insert(self.table[key])
            return self.table[key].val
        else:
            return -1
            
        

    def put(self, key: int, value: int) -> None:
        if key in self.table:          
            self.remove(self.table[key])
            
        self.table[key]=Node(key,value,None,None)
        self.insert(self.table[key])
        
        if len(self.table)>self.capacity:
            node=self.left.next
            self.remove(node)
            del self.table[node.key]


        
