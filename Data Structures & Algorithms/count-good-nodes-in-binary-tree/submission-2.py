'''
function call to check a node from the root is an eligible node that has no node in between that is greater
than the node being called. That function will 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def dfs(node,maxnode):
            if not node:
                return
            if maxnode<=node.val:
                self.count+=1
                maxnode=node.val

            
            dfs(node.left,maxnode)
            dfs(node.right,maxnode)
        dfs(root,float('-inf'))
        return self.count
            
        