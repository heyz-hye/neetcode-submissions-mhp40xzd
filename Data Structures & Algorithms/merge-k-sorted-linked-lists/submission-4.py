# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeList(self, lists1, lists2) -> ListNode:
        dummy=ListNode(0)
        cur=ListNode(0)
        cur=dummy
        while lists1 and lists2:
            if lists1.val<lists2.val:
                cur.next=lists1
                lists1=lists1.next
            else:
                cur.next=lists2
                lists2=lists2.next
            cur=cur.next

        if lists1:
                cur.next=lists1
        if lists2:
                cur.next=lists2

        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        while len(lists)>1:
            mlist=[]

            for i in range(0,len(lists),2):
                l1=lists[i]
                if i+1<len(lists):
                    l2=lists[i+1]
                else:
                    l2=None
                mlist.append(self.mergeList(l1,l2))
            lists=mlist
        return lists[0]


    
        