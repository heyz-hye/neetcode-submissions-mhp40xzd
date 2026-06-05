'''
if heights of node.left differ by height of node.right more than one return false
base case if no node return true
you search from the bottom up so we can avoid extra call stack saving run time
remember to use self because the variable is non local and you need to update and return the one
that is modify

the base condition in dfs changes this time if we detect ans==False we then immediately return 0
this save us from checking through the rest of the tree since it will just return 0 before we diverge
to left and right
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans=True
        def dfs(root) ->int:
            if not root or not self.ans:
                return 0
            left=dfs(root.left) 
            right=dfs(root.right)
            if abs(left-right)>1:
                self.ans=False
            return 1+max(left,right)
        dfs(root)
        return self.ans
        