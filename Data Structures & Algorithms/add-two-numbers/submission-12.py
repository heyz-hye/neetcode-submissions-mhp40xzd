# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        carryover=0
        while l1 or l2 or carryover:
            if l1:
                t=l1.val
            else:
                t=0
            if l2:
                t1=l2.val
            else:
                t1=0
            
            sum=t+t1+carryover
            carryover=sum//10
            sum=sum%10
            cur.next=ListNode(sum)
            cur=cur.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return dummy.next

        