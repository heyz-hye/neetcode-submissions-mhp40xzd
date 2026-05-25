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
        table={None:None}

        while cur:
            table[cur]=Node(cur.val)
            cur=cur.next

        cur=head

        while cur:
            table[cur].next=table[cur.next]
            table[cur].random=table[cur.random]
            cur=cur.next

        return table[head]



