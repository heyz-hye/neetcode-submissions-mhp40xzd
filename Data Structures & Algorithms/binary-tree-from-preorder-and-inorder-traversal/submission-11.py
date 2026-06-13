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

this solution is O(N)   since it avoid slicing  and O(N) space complexity because of hashmap
avoid O(N^2)space since it avoid storing those slicing subarray
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
        # 1. Map values to their indices in 'inorder' for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 2. Keep track of our current root in the preorder array
        self.preorder_idx = 0 
        
        # 3. Helper function that uses pointers (left and right bounds) instead of slicing
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            # Base case: if there are no elements to construct the tree
            if left > right:
                return None
            
            # Get the root value and increment the pointer for the next call
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            self.preorder_idx += 1
            
            # Find the root's split point in O(1) time
            mid = inorder_map[root_val]
            
            # Build left and right subtrees
            # Left subtree uses elements strictly before 'mid'
            root.left = array_to_tree(left, mid - 1)
            # Right subtree uses elements strictly after 'mid'
            root.right = array_to_tree(mid + 1, right)
            
            return root
            
        # Start the recursion spanning the entire array
        return array_to_tree(0, len(inorder) - 1)
    


        