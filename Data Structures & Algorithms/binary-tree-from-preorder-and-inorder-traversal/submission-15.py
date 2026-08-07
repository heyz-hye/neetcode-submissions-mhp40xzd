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
        table={value:index for index,value in enumerate(inorder)}
        self.preorder_ind=0
        left=0
        right=len(inorder)-1
        def left2right(left,right):
            if left>right:
                return None #cant do while or else infinite loop because left and right never change in first call
            root=TreeNode(preorder[self.preorder_ind])
            mid=table[preorder[self.preorder_ind]]
            self.preorder_ind+=1
            root.left=left2right(left,mid-1)
            root.right=left2right(mid+1,right)
            return root #you pass mid because of the inorder range you search from beginning to mid-1
        return left2right(left,right)

        
        