# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy=ListNode(0,head)
        fast=dummy # set both dummy node at beginning of the list and use fast and slow pointer, dummy to avoid none edgecases
        slow=dummy

        while fast and fast.next: # this ensure that we don't get None as fast
            fast=fast.next.next #fast travel twice as fast as slow ensuring that slow is in the middle of the list and fast is at the end
            slow=slow.next

        second=slow.next #this get the copy of slow.next 
        slow.next=None #break pointer of the first part of the list off the second part
        prev=None #set up prev to reverse pointer of the second part of the list
        
        while second:
            tmp=second.next #store the pointer to second.next so we can come back and iterate through the list
            second.next=prev #reverse the pointer backward
            prev=second      #for example, you have 5,6 for second part of the list. You store 6 as tmp, then you point to 5 which is second to None. Then move second to tmp second.next you previously stored
            second=tmp     #second now is the head of the end of the second part of the list

        first=head #merge here
        second=prev #second will be at none by the end of our second while loop so we have to set it to prev to get the head of sceond part of the list
        while second: #first is always going to be equal or larger size than second, if there is no second we leave first as is since there already exist the pointer to our last element
            tmp2=first.next #store each next pointer to merge the pointers
            tmp3=second.next
            first.next=second
            second.next=tmp2 #while there is second left to append we append
            first=tmp2
            second=tmp3
        




        