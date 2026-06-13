'''
"""
Construct Binary Tree from Preorder and Inorder Traversals

Core Logic:
1. Root Identification: `preorder[0]` is always the root of the current tree.
2. Subtree Partitioning: Finding the root's index in `inorder` (the `mid` index) 
   cleanly splits the left and right subtrees.
   - Elements before `mid` in `inorder` belong to the Left Subtree.
   - Elements after `mid` in `inorder` belong to the Right Subtree.

Recursive Steps:
- Base Case: If the arrays are empty, we've gone past a leaf node. Return None.
- Get the root value from preorder[0] and find its index (`mid`) in inorder.
- Slice the arrays to get the exact elements for the next recursive calls:
    -> Left Subtree: inorder[:mid] and preorder[1 : mid+1]
    -> Right Subtree: inorder[mid+1:] and preorder[mid+1:]
    we can to return root since root we assign root.left and root.right to the value of our recrusive call
    we can exclude passing first index for our left subtree since that will always be our root/subroot and we
    have already make a TreeNode for it in our recursive call
    this is the right version
    
"""
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

        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
    


        