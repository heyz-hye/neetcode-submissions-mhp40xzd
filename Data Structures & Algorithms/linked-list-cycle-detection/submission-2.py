# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        smap={}

        curr=head

        while curr:
            if curr.next in smap:
                return True
            
            smap[curr]=1

            curr=curr.next

        return False

        