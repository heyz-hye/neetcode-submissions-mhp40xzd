# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def verify(root,subroot):
            if (not root and not subroot):
                return True
            if (not root or not subroot) or (root.val!=subroot.val):
                return False
            
            return verify(root.left,subroot.left) and verify(root.right,subroot.right)
        
        if not root or not subRoot:
            return False
        
        if verify(root,subRoot): #if one root and subroot node match and verify return false that doesnt mean that cant be another node that match and verify return true for the subtree
            return True #error early return False ending the entire exploration early
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        


        
        