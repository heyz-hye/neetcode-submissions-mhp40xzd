'''
this solution is quite not as optimal because it uses a Log n call stack. I will be posting a solution
that is more optimal under this comment:
first of all problem statement you need to find the lowest common ancestor and anscestor can be the descedent
of itself.
edge case if there is not a root you return null, if p and q are null you return root
so starting from the beginning of the node you can recursively call the function until a solution is reach.
here is the base condtions: if p and q are all less than root you call to the root.left if p and q is all
greater than the root you call root.left. if one of them is equal that means one of them is the ancestor of itself
and other. if p is encounter fisrt then q must be deep within p somewhere and vice versa.  since all the nodes
are unique that means if all the node under p and q cannot become a ancestor of p and q. the first root that is 
the ancestor of p and q will be the lowest common ancestor. The ancestor is either one of p or q or the first node
that is the ancestor of p and q

O(1)space complexity solution
cur=root
while cur:
    if cur.val>p.val and cur.val>q.val:
        cur=cur.right
    elif cur.val<p.val and cur.val<q.val:
        cur=cur.left
    else:
        return cur
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur=root
        while cur:
            if cur.val>p.val and cur.val>q.val:
                cur=cur.left
            elif cur.val<p.val and cur.val<q.val:
                cur=cur.right
            else:
                return cur
        