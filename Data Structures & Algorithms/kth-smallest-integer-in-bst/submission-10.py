# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans=[]
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            self.ans.append(node.val) #first method dont work because you add even if node is None, if you move append at the bottom it will append every single node from the bottom postorder traversal so you need to append right after the left traversal
            dfs(node.right)
            
        dfs(root)
        return self.ans[k-1]


        

        