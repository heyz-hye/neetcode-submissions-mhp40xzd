'''
dfs travel for both tree and cehck if each node value is equal to each other if they are return True else False
or return the first condition that is truthy
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: #this checks if both are false
            return True
        
        if not p or not q: #since the top condition above check if both are null we use or here to see the whether one of is true
            return False

        if p.val!=q.val:
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        