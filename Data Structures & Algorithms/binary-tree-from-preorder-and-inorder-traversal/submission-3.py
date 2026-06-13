'''
pretty tricky question: so we know that inorder traversal visit from left bottom up to the root and the visit the right tree.
preorder traversal visit top to left bottom and then right top to bottom. But knowing these facts we can know which node below to
the left subtree and right subtree. we can start from inorder traversal and traverse from bottom to the root. Since we know preorder
always start from the root, any time our nodes matches in preorder traversal we know that you have finish traveersing left subtree.
we always know that if we encounter the root, the nodes before we encounter the root in inorder traversal will be our left subtree.
we can match those nodes to right of preorder subtree to give us our left subtree. Then the remainder of the nodes in preorder traversal belong
to the right subtree

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0])

        mid=inorder.index(preorder[0]) # find index of the root in inorder

        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid+1])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
    


        