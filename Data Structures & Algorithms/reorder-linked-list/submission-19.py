# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head
        array=[]

        while curr:
            array.append(curr)
            curr=curr.next

        reverse_array=array[::-1]

        curr=head

        for i in range(len(reverse_array)//2):           
            nodelist=curr.next
            curr.next=reverse_array[i]
            curr=curr.next
            curr.next=nodelist
            curr=curr.next
        curr.next=None


        