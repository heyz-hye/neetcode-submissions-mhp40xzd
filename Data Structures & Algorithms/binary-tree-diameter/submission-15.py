class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  # Global tracker for the longest chain of edges

        def get_height(node):
            if not node:
                return 0
            
            # Get the max edge-height of left and right subtrees
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # The diameter at THIS specific node is left edges + right edges
            current_diameter = left_height + right_height
            
            # Update our global maximum if this local path is wider
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return the height of this node to its parent
            return 1 + max(left_height, right_height)

        get_height(root)
        return self.max_diameter