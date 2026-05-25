"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur=head
        table={None:None} #random contains null pointer

        while cur:
            table[cur]=Node(cur.val) # this create a copy of the node, cur.next and random wasnt seen yet if you use cur.val as key we lose data if cur.val have duplicate and overwriting
            cur=cur.next

        cur=head

        while cur:
            table[cur].next=table[cur.next]
            table[cur].random=table[cur.random]
            cur=cur.next

        return table[head]



