'''
Exactly — that's the core idea.

index = the position of the root in inorder, which is the same thing as the count of nodes to its left in inorder. 
Since everything left of the root in inorder is the entire left subtree, index tells you the size of the left subtree.

That size is what you then use to cut preorder, because preorder lists the root, then all index left-subtree nodes back-to-back, 
then the right subtree. So:

preorder[0] → root
preorder[1 : 1+index] → next index elements → the whole left subtree
preorder[1+index :] → whatever's left → the whole right subtree

It's a nice pattern to internalize for tree-reconstruction problems generally: 
inorder tells you subtree sizes (via where the root sits), 
and you use those sizes to slice preorder/postorder correctly. 
Same logic shows up if you ever do "Construct Binary Tree from Inorder and Postorder Traversal."

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
        index=inorder.index(preorder[0])
        
        root.left=self.buildTree(preorder[1:index+1],inorder[:index])
        root.right=self.buildTree(preorder[index+1:],inorder[index+1:])

        return root
        