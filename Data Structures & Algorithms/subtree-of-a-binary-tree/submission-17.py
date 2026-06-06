# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    

       
class Solution:
    def isSameTree(self,root,subroot)->bool:

        if not root and not subroot:
            return True

        if not root or not subroot:
            return False

        if root.val!=subroot.val:
            return False

        return self.isSameTree(root.left,subroot.left) and self.isSameTree(root.right,subroot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val==subRoot.val:
            if self.isSameTree(root,subRoot):
                return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    