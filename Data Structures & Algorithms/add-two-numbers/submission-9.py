# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode() #avoid null case
        cur=dummy
        carryover=0
        while l1 or l2 or carryover:
            if l1:
                s1=l1.val
            else:
                s1=0

            if l2:
                s2=l2.val
            else:
                s2=0

            sum=s1+s2+carryover
            carryover=sum//10 #if two number of different length add and their digit addition exceed 10 this create a carryover which prompt us to create a new node
            sum=sum%10 #this ensure that num we create new node with is always less than 10

            cur.next=ListNode(sum)
            cur=cur.next
            
            if l1:
                l1=l1.next #if it is l1.next condition check then the pointer will be stuck at last forever
            if l2:
                l2=l2.next #check if there is a l1 and l2 to move onto, or else you get none.next which is error
        
        return dummy.next

        
            

        