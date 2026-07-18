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
        positiveinf=float("inf")
        negativeinf=float("-inf")
        def dfs(neg,root,pos)->bool:
            if not root:
                return True
            
            if root.val<=neg or root.val>=pos:
                return False
            
            return dfs(neg,root.left,root.val) and dfs(root.val,root.right,pos)

        return dfs(negativeinf,root,positiveinf)