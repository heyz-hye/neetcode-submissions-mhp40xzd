# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=float("-inf")
        def dfs(node):
            if not node:
                return 0
            
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))


            s=node.val+left+right
            self.maxsum=max(self.maxsum,s)
            node.val+=max(0,max(left,right))
            return node.val
        
        dfs(root)
        return self.maxsum


        