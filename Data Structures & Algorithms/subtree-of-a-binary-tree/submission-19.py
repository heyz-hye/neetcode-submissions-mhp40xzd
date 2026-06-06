# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    

       
class Solution:
    def isSameTree(self,root,subroot)->bool: #answer from the last question

        if not root and not subroot:
            return True

        if not root or not subroot:
            return False

        if root.val!=subroot.val:
            return False

        return self.isSameTree(root.left,subroot.left) and self.isSameTree(root.right,subroot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot: #if there is no root or subRoot to compare to you return 
            return False
        if root.val==subRoot.val: #this is avoid extra call stack you can remove it and it still True
            if self.isSameTree(root,subRoot): #there is a case that even though the root match but the subtree isn't the same still
                return True                   
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)#keep calling until the subroot match with root's subtree
    