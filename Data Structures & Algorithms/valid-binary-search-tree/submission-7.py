# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans=True
        posinf=TreeNode(float('inf'))
        neginf=TreeNode(float('-inf'))
        def check(root,left,right):
            if not root:
                return
            if left.val>=root.val or root.val >= right.val:
                self.ans=False
            check(root.left,left,root)
            check(root.right,root,right)

        check(root,neginf,posinf)

        return self.ans
            


        