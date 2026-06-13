'''
pretty tricky question: so we know that inorder traversal visit from left bottom up to the root and the visit the right tree.
preorder traversal visit top to left bottom and then right top to bottom. But knowing these facts we can know which node below to
the left subtree and right subtree. we can start from inorder traversal and traverse from bottom to the root. Since we know preorder
always start from the root, any time our nodes matches in preorder traversal we know that you have finish traveersing left subtree.
we always know that if we encounter the root, the nodes before we encounter the root in inorder traversal will be our left subtree.
we can match those nodes to right of preorder subtree to give us our left subtree. Then the remainder of the nodes in preorder traversal belong
to the right subtree

root=preorder[0]
by finding the index of the root in inorder we can tell which elements belong to the left and right subtree
the length of the elment of the left subtree and right tree in both traversal is equal. So we know that preorder
go from root to every node in the left first before going right. and inorder goes from every node from the bottom
left to the root. if we have the index of the root in inorder we can get the subarray we need for the left subtree
in preorder traversal.
example:
preorder:
[0,1,2]
inorder:
[1,0,2]

the index of the root in inorder is 1 we call this our mid index(this separate left and right) 
by getting the index
we know in preorder that from index 1 to 1(excluding the root itself) it belong the left subtree
we can continually pass in the the subarray of both traversal for left and right subtrees in our recursion
since in our recursion we we always start from index one instead of 0 we will eventaully encounter a situation
where both the inital starting index of our slicing will go past the mid index, this will give us an empty array.
the edge case in this case is to check if there is an empty we can't do go further so we return None.

in every single recurisve we always make the first index of preorder out root and then we set
root.left=recursive cal(left subtree partition of preorder exluding the first element, left subtree partition of inorder)
root.right=recurisve call(right subtree partition from mid+1 index to the very end, right subtree partition also the same as preorder)

most important thing:since preorder go from root to left then right we are always sure that it overlap with inorder
because inorder goes from bottom left to root. so we always gurantee the first portion of both traversal always overlap
in elements
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
    


        