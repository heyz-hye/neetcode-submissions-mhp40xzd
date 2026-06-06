'''
it says lowest commmon ancestor so a dfs would be suitable because it scan from bottom up
using the dfs approach you can travel to the bottom of the tree and go up from there
every node has a descendant of p and q
edge condition if there is only a single node it can be anscestor with itself
stop condtion or base statement: if there is no node for root.left and no node for root.right
return root and if there is no root also return null
if condition should be below every recurusive call

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return null
        if not p and not q:
            return root
        if p.val>root.val and q.val<root.val:
            return root
        if p.val<root.val and q.val>root.val:
            return root
        if p.val==root.val or q.val==root.val:
            return root
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        