'''
My initial approach is to check left and right subtree to make sure that every node in left subtree is less than
the root node and every right node in right subtree is less than the root node. This run O(N) time, then we
check if the children of the node is valid for every node. This also take O(N) so if you multiply then together 
it will take O(N) square time. However there is a way where you can do both and still get it down to O(N) time
the solution require you to start the recursive call with positive and negative infinity as left and right TreeNode
you first compare if root is less than infinity and greater than negative infinity. Then for root.left you pass in
root as the upperbound and negative infinity as the lowebound. For root.right you pass in positive infinity as the
upperbound and root itself as the lowerbound. For left recrusive call the children will always inherit the parent's
lowerbound and get the root itself as upperbound. For right recursive call the children will inherit the
parent's upperbound and get tehe root as teh lowerbound
'''
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
            


        