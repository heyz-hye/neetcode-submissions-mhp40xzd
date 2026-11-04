'''
return true too fast only return true if it hit the base case of not having any nodes to explore
if you return too fast then you only check the first node and no one else you need to recursive down
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pos=float("inf")
        neg=float("-inf")

        def dfs(node,p,n):
            if not node:
                return True
            
            if node.val>=p or node.val<=n:
                return False
            
            return dfs(node.left,node.val,n) and dfs(node.right,p,node.val)
        return dfs(root,pos,neg)
        